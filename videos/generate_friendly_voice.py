import asyncio
import edge_tts
from pathlib import Path
import subprocess
import json

SCRIPT_TEXT = (
    "¡Qué tal amigos! ¿A poco no da mucho pendiente cuando se te estrella la pantalla de tu celular? "
    "Y es que da desconfianza llevarlo a las plazas... donde se quedan con tu teléfono días enteros, "
    "y la neta da miedo que te revisen tus fotos personales o le quiten piezas. "
    "¡Por eso en Volt Repair Studio lo hacemos diferente! "
    "Nosotros vamos directo a tu casa, nos sentamos en tu mesa y en 25 minutos cambiamos tu pantalla frente a ti. "
    "Desarmamos con desarmadores de precisión, levantamos la pantalla con ventosa sin rayar tu marco, "
    "y desconectamos la batería de inmediato por tu seguridad. "
    "Además, usamos programadora de microchips para transferir tu True Tone y los 120 Hertz, "
    "instalando pantalla certificada con colores idénticos de fábrica. "
    "Probamos el táctil y sensores contigo presente, te damos 90 días de garantía por escrito "
    "y la mano de obra es fija de solo 700 pesitos. "
    "¡Mándanos un WhatsApp hoy mismo y te cotizo de volada!"
)

async def generate():
    out_dir = Path(r"C:\Users\SAmue\Desktop\Volt-Repair-Studio\remotion_reels\public")
    audio_path = out_dir / "volt_voice_friendly.mp3"
    
    # Generate with es-US-AlonsoNeural (warm, youthful, highly conversational Mexican-American tone)
    communicate = edge_tts.Communicate(text=SCRIPT_TEXT, voice="es-US-AlonsoNeural", rate="+2%", pitch="+0Hz")
    await communicate.save(str(audio_path))
    print(f"Generated friendly audio at: {audio_path}")
    
    # Also generate Dalia version just in case
    dalia_path = out_dir / "volt_voice_dalia.mp3"
    communicate_dalia = edge_tts.Communicate(text=SCRIPT_TEXT, voice="es-MX-DaliaNeural", rate="+3%", pitch="+0Hz")
    await communicate_dalia.save(str(dalia_path))
    print(f"Generated Dalia audio at: {dalia_path}")

    # Inspect duration with ffprobe
    for p in [audio_path, dalia_path]:
        cmd = [
            "ffprobe", "-v", "error", "-show_entries", "format=duration",
            "-of", "default=noprint_wrappers=1:nokey=1", str(p)
        ]
        res = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        dur = float(res.stdout.strip())
        print(f"File: {p.name} -> Duration: {dur:.2f} seconds ({int(dur * 30)} frames at 30fps)")

if __name__ == "__main__":
    asyncio.run(generate())
