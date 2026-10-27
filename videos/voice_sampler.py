import asyncio
import edge_tts
from pathlib import Path

sample_text = "¡Hola! ¿Alguna vez te ha dado miedo llevar tu celular a reparar por temor a que le cambien piezas o te revisen tus fotos? En Volt Repair Studio te lo arreglamos en tu propia sala y frente a tus ojos. ¡Mándanos un mensajito!"

out_dir = Path(r"C:\Users\SAmue\Desktop\Volt-Repair-Studio\videos\b_roll\voice_tests")
out_dir.mkdir(parents=True, exist_ok=True)

async def test_voices():
    configs = [
        ("es-US-AlonsoNeural", "+2%", "+0Hz", "alonso_friendly.mp3"),
        ("es-MX-DaliaNeural", "+3%", "+0Hz", "dalia_warm.mp3"),
        ("es-MX-JorgeNeural", "+1%", "-1Hz", "jorge_close.mp3"),
    ]
    for v, r, p, fname in configs:
        target = out_dir / fname
        c = edge_tts.Communicate(text=sample_text, voice=v, rate=r, pitch=p)
        await c.save(str(target))
        print(f"Generated: {fname} with {v} (size: {target.stat().st_size} bytes)")

if __name__ == "__main__":
    asyncio.run(test_voices())
