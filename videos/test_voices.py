import asyncio
import edge_tts

async def main():
    voices = await edge_tts.list_voices()
    for v in voices:
        loc = v.get("Locale", "")
        if loc.startswith("es-MX") or loc in ["es-US", "es-CO"]:
            print(f"{v['ShortName']:25} | {v['Gender']:6} | {loc} | {v.get('FriendlyName','')}")

if __name__ == "__main__":
    asyncio.run(main())
