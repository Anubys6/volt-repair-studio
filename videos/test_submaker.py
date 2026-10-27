import asyncio
import edge_tts
import json

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

async def test_sub():
    comm = edge_tts.Communicate(text=SCRIPT_30S, voice="es-US-AlonsoNeural", rate="+6%")
    submaker = edge_tts.SubMaker()
    async for chunk in comm.stream():
        if chunk["type"] == "audio":
            pass
        elif chunk["type"] == "WordBoundary":
            submaker.create_sub((chunk["offset"], chunk["duration"]), chunk["text"])
    
    print("Generated Subtitle text length:", len(submaker.get_srt()))
    print("SRT sample:\n", submaker.get_srt()[:600])

if __name__ == "__main__":
    asyncio.run(test_sub())
