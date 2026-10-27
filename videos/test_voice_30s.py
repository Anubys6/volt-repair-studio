import asyncio
import edge_tts
import imageio_ffmpeg
import subprocess
from pathlib import Path

SCRIPT_PUNCHY = (
    "¡Qué onda amigos! Si se te estrelló la pantalla de tu celular y te da miedo llevarlo a las plazas "
    "donde se lo quedan días o revisan tus fotos... ¡en Volt Repair Studio lo hacemos en tu comedor! "
    "Vamos directo a tu domicilio y en 25 minutos cambiamos tu display frente a ti. "
    "Desarmamos con precisión, desconectamos batería por seguridad, y usamos programadora de microchips "
    "para conservar tu True Tone y los 120 Hertz originales. "
    "Instalamos refacción certificada Grado A Plus, probamos el táctil contigo presente, "
    "y la mano de obra es fija de solo 700 pesitos con 90 días de garantía. "
    "¡Mándanos un WhatsApp hoy mismo y te cotizo de volada!"
)

async def test_timing():
    out_dir = Path(r"C:\Users\SAmue\Desktop\Volt-Repair-Studio\remotion_reels\public")
    audio_path = out_dir / "volt_voice_friendly_30s.mp3"
    
    # Generate with es-US-AlonsoNeural with +6% rate (conversational, energetic TikTok pace)
    communicate = edge_tts.Communicate(text=SCRIPT_PUNCHY, voice="es-US-AlonsoNeural", rate="+6%", pitch="+0Hz")
    await communicate.save(str(audio_path))
    
    ffmpeg = imageio_ffmpeg.get_ffmpeg_exe()
    res = subprocess.run([ffmpeg, "-i", str(audio_path)], stderr=subprocess.PIPE, text=True)
    for line in res.stderr.splitlines():
        if "Duration:" in line:
            print("Audio Duration:", line.strip())

if __name__ == "__main__":
    asyncio.run(test_timing())
