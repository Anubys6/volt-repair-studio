import asyncio
import edge_tts

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

async def check():
    c = edge_tts.Communicate(SCRIPT_PUNCHY, "es-US-AlonsoNeural", rate="+6%")
    async for chunk in c.stream():
        if chunk['type'] == 'SentenceBoundary':
            start_sec = chunk['offset'] / 10_000_000
            dur_sec = chunk['duration'] / 10_000_000
            end_sec = start_sec + dur_sec
            start_frame = int(start_sec * 30)
            end_frame = int(end_sec * 30)
            print(f"[{start_sec:5.2f}s - {end_sec:5.2f}s | F{start_frame:4d}-F{end_frame:4d}] {chunk['text']}")

if __name__ == "__main__":
    asyncio.run(check())
