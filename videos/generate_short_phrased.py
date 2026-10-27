import asyncio
import edge_tts
import imageio_ffmpeg
import subprocess
from pathlib import Path

# Short, punchy, conversational, high-energy for 30s TikTok/Reels format
SHORT_PHRASES = [
    "¡Qué onda amigos!",
    "¿Se te estrelló la pantalla de tu celular?",
    "¡No lo dejes días en plazas con miedo a que revisen tus fotos!",
    "En Volt Repair Studio vamos directo a tu domicilio.",
    "Cambiamos tu display en tu comedor en 25 minutos frente a tus ojos.",
    "Desarmamos con precisión y quitamos tornillos pentalobe.",
    "Abrimos con ventosa especial sin rayar tu marco.",
    "Desconectamos la batería para proteger tus circuitos.",
    "Transferimos tu True Tone con programadora de microchips.",
    "Instalamos pantalla certificada Grado A Plus.",
    "Probamos táctil y sensores contigo presente.",
    "Mano de obra fija de 700 pesitos y 90 días de garantía.",
    "¡Mándanos WhatsApp y te cotizo de volada!"
]

FULL_SHORT = " ".join(SHORT_PHRASES)

async def run_short():
    out_dir = Path(r"C:\Users\SAmue\Desktop\Volt-Repair-Studio\remotion_reels\public")
    audio_path = out_dir / "volt_voice_alonso_short_30s.mp3"
    
    # es-US-AlonsoNeural with +10% rate for natural, upbeat social media pace
    c = edge_tts.Communicate(FULL_SHORT, "es-US-AlonsoNeural", rate="+10%")
    
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

    print(f"\n--- {len(boundaries)} SENTENCES (Total: {total_dur:.2f}s) ---")
    for i, b in enumerate(boundaries):
        s_sec = b["offset"] / 10_000_000
        d_sec = b["duration"] / 10_000_000
        e_sec = s_sec + d_sec
        s_f = int(s_sec * 30)
        e_f = int(e_sec * 30)
        dur_f = e_f - s_f
        print(f"Scene {i+1:02d}: [{s_sec:5.2f}s - {e_sec:5.2f}s | F{s_f:4d}-F{e_f:4d} ({dur_f:3d}f, {d_sec:4.2f}s)] {b['text']}")

if __name__ == "__main__":
    asyncio.run(run_short())
