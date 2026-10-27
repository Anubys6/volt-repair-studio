import asyncio
import edge_tts

async def main():
    voices = await edge_tts.list_voices()
    es_voices = [v for v in voices if v['Locale'].startswith('es-')]
    for v in es_voices:
        print(f"{v['ShortName']:25} | {v['Gender']:6} | {v['Locale']}")

if __name__ == "__main__":
    asyncio.run(main())
