import asyncio
import edge_tts
import imageio_ffmpeg
import subprocess
from pathlib import Path

PHRASES = [
    "¡Qué onda amigos!",
    "¿Se te estrelló la pantalla de tu celular?",
    "Seguro te da miedo llevarlo a las plazas...",
    "donde se quedan con tu teléfono por días enteros,",
    "o temes que revisen tus fotos personales y tus datos.",
    "¡En Volt Repair Studio lo hacemos completamente diferente!",
    "Nosotros vamos directo hasta tu casa u oficina.",
    "Y en 25 minutos cambiamos tu display frente a tus propios ojos.",
    "Desarmamos con desarmadores de precisión.",
    "Abrimos con ventosa especial sin rayar el marco.",
    "Desconectamos la batería de inmediato por tu seguridad.",
    "Usamos programadora de microchips para transferir tu True Tone y los 120 Hertz.",
    "Instalamos pantalla certificada Grado A Plus con colores de fábrica.",
    "Probamos el multitouch y los sensores contigo presente.",
    "Mano de obra fija de solo 700 pesitos y 90 días de garantía por escrito.",
    "¡Mándanos un WhatsApp hoy mismo y te cotizo de volada!"
]

FULL_TEXT = " ".join(PHRASES)

async def run():
    out_dir = Path(r"C:\Users\SAmue\Desktop\Volt-Repair-Studio\remotion_reels\public")
    audio_path = out_dir / "volt_voice_alonso_phrases.mp3"
    
    # es-US-AlonsoNeural with +4% rate for friendly, natural pacing
    c = edge_tts.Communicate(FULL_TEXT, "es-US-AlonsoNeural", rate="+4%")
    
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
            # extract seconds
            parts = line.split("Duration:")[1].split(",")[0].strip().split(":")
            total_dur = float(parts[0])*3600 + float(parts[1])*60 + float(parts[2])

    print(f"\n--- {len(boundaries)} SENTENCE BOUNDARIES (Total: {total_dur:.2f}s) ---")
    for i, b in enumerate(boundaries):
        s_sec = b["offset"] / 10_000_000
        d_sec = b["duration"] / 10_000_000
        e_sec = s_sec + d_sec
        s_f = int(s_sec * 30)
        e_f = int(e_sec * 30)
        dur_f = e_f - s_f
        print(f"Scene {i+1:02d}: [{s_sec:5.2f}s - {e_sec:5.2f}s | F{s_f:4d}-F{e_f:4d} ({dur_f:3d} frames, {d_sec:4.2f}s)] {b['text']}")

if __name__ == "__main__":
    asyncio.run(run())
