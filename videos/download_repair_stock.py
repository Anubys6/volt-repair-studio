import os
import sys
import json
import time
import urllib.request
import urllib.parse
from pathlib import Path
from PIL import Image

if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

STOCK_DIR = Path(r"C:\Users\SAmue\Desktop\Volt-Repair-Studio\videos\b_roll\stock_repair")
STOCK_DIR.mkdir(parents=True, exist_ok=True)

CATEGORIES = [
    ("iPhone Display Repair", ["IPhone display repair", "IPhone 6s display repair", "phone screen replacement"]),
    ("iPhone Teardown & Logic Board", ["IPhone teardown", "IPhone disassembly", "Apple A15 logic board"]),
    ("Samsung & Android Repair", ["Samsung Galaxy teardown", "Samsung Galaxy repair", "smartphone disassembly"]),
    ("Microscope & Microsoldering", ["electronics repair microscope", "surface mount soldering microscope", "soldering circuit board"]),
    ("Tools & Workbench", ["smartphone repair workbench", "pentalobe screwdriver", "cellphone repair"])
]

all_items = []

print("🔍 Conectando con repositorio técnico de Wikimedia Commons...")

for cat_name, query_list in CATEGORIES:
    for q in query_list:
        url = (
            f"https://commons.wikimedia.org/w/api.php?action=query&generator=search"
            f"&gsrsearch={urllib.parse.quote(q)}&gsrnamespace=6&gsrlimit=10"
            f"&prop=imageinfo&iiprop=url|size|mime&iiurlwidth=1280&format=json"
        )
        req = urllib.request.Request(url, headers={"User-Agent": "VoltRepairStudio/2.0 (contact@voltrepair.mx)"})
        try:
            with urllib.request.urlopen(req, timeout=10) as resp:
                data = json.loads(resp.read().decode("utf-8"))
                pages = data.get("query", {}).get("pages", {})
                for pid, p in pages.items():
                    title = p.get("title", "")
                    tl = title.lower()
                    if any(bad in tl for bad in ["bicycle", "train", "car", "station", "building", "church", "ship", "bridge", "rail"]):
                        continue
                    info = p.get("imageinfo", [{}])[0]
                    thumb = info.get("thumburl") or info.get("url")
                    if thumb and any(ext in thumb.lower() for ext in [".jpg", ".jpeg", ".png", ".webp"]):
                        all_items.append({
                            "title": title,
                            "url": thumb,
                            "category": cat_name
                        })
        except Exception as e:
            pass
        time.sleep(0.2)

# Deduplicar
seen = set()
unique_items = []
for it in all_items:
    if it["url"] not in seen:
        seen.add(it["url"])
        unique_items.append(it)

print(f"✅ Se localizaron {len(unique_items)} fotografías técnicas especializadas.")

downloaded = []
for idx, it in enumerate(unique_items[:30], 1):
    filename = f"tech_stock_{idx:02d}.jpg"
    dest = STOCK_DIR / filename
    if dest.exists() and dest.stat().st_size > 15000:
        downloaded.append(dest)
        continue

    print(f"   [{idx}/{min(30, len(unique_items))}] Descargando: {it['title'][:55]}...")
    try:
        req = urllib.request.Request(it["url"], headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"})
        with urllib.request.urlopen(req, timeout=12) as res, open(dest, "wb") as f:
            f.write(res.read())

        with Image.open(dest) as img:
            img.verify()
        downloaded.append(dest)
        print(f"       ✓ Guardada ({dest.stat().st_size // 1024} KB)")
    except Exception as e:
        print(f"       ✗ Error: {e}")
        if dest.exists():
            dest.unlink()
    time.sleep(0.3)

print(f"\n🎉 Total de fotografías listas: {len(downloaded)} en {STOCK_DIR}")
