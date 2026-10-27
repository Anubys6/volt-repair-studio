import asyncio
import edge_tts
import imageio_ffmpeg
import subprocess
from pathlib import Path

REEL3_PHRASES = [
    "¡Qué onda amigos!",
    "¡Mucho cuidado con cómo te cambian la batería de tu celular en la calle!",
    "¿Tu teléfono se descarga en pocas horas o se calienta demasiado?",
    "Hemos abierto equipos donde pegaron la batería con cinta escolar doble cara o resistol.",
    "Eso deforma la celda, sobrecalienta el procesador y arruina tu equipo.",
    "¡En Volt Repair Studio lo hacemos con estándar de fábrica!",
    "Vamos directo a tu domicilio y en 20 minutos cambiamos tu batería frente a ti.",
    "Retiramos la batería vieja con pinzas de precisión sin doblar los componentes.",
    "Instalamos celda de alta densidad con sus tiras térmicas elásticas pull-tabs originales.",
    "Disipan el calor y restauran la salud de tu batería al 100%.",
    "Mano de obra garantizada de solo 500 pesitos con 90 días de garantía por escrito.",
    "¡Mándanos un WhatsApp hoy mismo y estrena batería de volada!"
]

FULL_TEXT_3 = " ".join(REEL3_PHRASES)

async def run_reel3():
    out_dir = Path(r"C:\Users\SAmue\Desktop\Volt-Repair-Studio\remotion_reels\public")
    audio_path = out_dir / "volt_voice_reel3_bateria.mp3"
    
    c = edge_tts.Communicate(FULL_TEXT_3, "es-US-AlonsoNeural", rate="+10%")
    
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

    print(f"\n--- REEL 3: {len(boundaries)} SENTENCES (Total: {total_dur:.2f}s) ---")
    for i, b in enumerate(boundaries):
        s_sec = b["offset"] / 10_000_000
        d_sec = b["duration"] / 10_000_000
        e_sec = s_sec + d_sec
        s_f = int(s_sec * 30)
        e_f = int(e_sec * 30)
        dur_f = e_f - s_f
        print(f"Scene {i+1:02d}: [{s_sec:5.2f}s - {e_sec:5.2f}s | F{s_f:4d}-F{e_f:4d} ({dur_f:3d}f, {d_sec:4.2f}s)] {b['text']}")

if __name__ == "__main__":
    asyncio.run(run_reel3())
