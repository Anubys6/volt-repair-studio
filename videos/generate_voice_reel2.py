import asyncio
import edge_tts
import imageio_ffmpeg
import subprocess
from pathlib import Path

REEL2_PHRASES = [
    "¡Qué onda amigos!",
    "¿Sabías que si cambias la pantalla de tu iPhone en la calle pierdes el True Tone?",
    "¡Y además el brillo automático se vuelve loco!",
    "Eso pasa porque los talleres no transfieren el número de serie de tu pantalla vieja.",
    "¡En Volt Repair Studio lo hacemos con nivel de laboratorio!",
    "Vamos directo a tu casa con nuestra programadora JCID.",
    "Conectamos tu pantalla rota y extraemos el serial criptográfico del microchip.",
    "Luego lo transferimos a tu nueva pantalla certificada Grado A Plus.",
    "Así conservas tus colores de fábrica, tu True Tone y los 120 Hertz.",
    "Hacemos calibración y pruebas en vivo frente a ti en 25 minutos.",
    "Mano de obra fija de solo 700 pesitos con 90 días de garantía por escrito.",
    "¡Mándanos un WhatsApp hoy mismo y te cotizo de volada!"
]

FULL_TEXT_2 = " ".join(REEL2_PHRASES)

async def run_reel2():
    out_dir = Path(r"C:\Users\SAmue\Desktop\Volt-Repair-Studio\remotion_reels\public")
    audio_path = out_dir / "volt_voice_reel2_truetone.mp3"
    
    c = edge_tts.Communicate(FULL_TEXT_2, "es-US-AlonsoNeural", rate="+10%")
    
    boundaries = []
    with open(audio_path, "wb") as f:
        async for chunk in c.stream():
            if chunk["type"] == "audio":
                f.write(chunk["data"])
            elif chunk["type"] == "SentenceBoundary":
                boundaries.append(chunk)

    ffmpeg = imageio_ffmpeg.get_ffmpeg_exe()
    res = subprocess.run([ffmpeg, "-i", str(audio_path)], stderr=subprocess.PIPE, text=True)
    total_dur = None
    for line in res.stderr.splitlines():
        if "Duration:" in line:
            print("Total Duration:", line.strip())
            parts = line.split("Duration:")[1].split(",")[0].strip().split(":")
            total_dur = float(parts[0])*3600 + float(parts[1])*60 + float(parts[2])

    print(f"\n--- REEL 2: {len(boundaries)} SENTENCES (Total: {total_dur:.2f}s) ---")
    for i, b in enumerate(boundaries):
        s_sec = b["offset"] / 10_000_000
        d_sec = b["duration"] / 10_000_000
        e_sec = s_sec + d_sec
        s_f = int(s_sec * 30)
        e_f = int(e_sec * 30)
        dur_f = e_f - s_f
        print(f"Scene {i+1:02d}: [{s_sec:5.2f}s - {e_sec:5.2f}s | F{s_f:4d}-F{e_f:4d} ({dur_f:3d}f, {d_sec:4.2f}s)] {b['text']}")

if __name__ == "__main__":
    asyncio.run(run_reel2())
