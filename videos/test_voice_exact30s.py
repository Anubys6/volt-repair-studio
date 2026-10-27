import asyncio
import edge_tts
import imageio_ffmpeg
import subprocess
from pathlib import Path

SCRIPT_30S = (
    "¡Qué onda amigos! Si se te estrelló la pantalla de tu cel y te da miedo dejarlo días en plazas "
    "donde revisan tus fotos... ¡en Volt Repair Studio vamos directo a tu casa! "
    "Cambiamos tu display en tu comedor en 25 minutos frente a tus ojos. "
    "Desarmamos con precisión, desconectamos batería por seguridad, "
    "y usamos programadora de microchips para transferir tu True Tone y los 120 Hertz. "
    "Instalamos pantalla certificada Grado A Plus, con mano de obra fija de solo 700 pesitos "
    "y 90 días de garantía por escrito. "
    "¡Mándanos un WhatsApp hoy mismo y te cotizo de volada!"
)

async def test():
    out_dir = Path(r"C:\Users\SAmue\Desktop\Volt-Repair-Studio\remotion_reels\public")
    audio_path = out_dir / "volt_voice_alonso_30s.mp3"
    
    # Generate with es-US-AlonsoNeural +6%
    comm = edge_tts.Communicate(text=SCRIPT_30S, voice="es-US-AlonsoNeural", rate="+6%")
    await comm.save(str(audio_path))
    
    ffmpeg = imageio_ffmpeg.get_ffmpeg_exe()
    res = subprocess.run([ffmpeg, "-i", str(audio_path)], stderr=subprocess.PIPE, text=True)
    for line in res.stderr.splitlines():
        if "Duration:" in line:
            print("Alonso Duration:", line.strip())

if __name__ == "__main__":
    asyncio.run(test())
