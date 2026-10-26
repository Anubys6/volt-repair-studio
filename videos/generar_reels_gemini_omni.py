"""
=============================================================================
⚡ GENERADOR DE REELS VOLT REPAIR STUDIO: VEO 3.1 & GEMINI OMNI FLASH
=============================================================================
Este script unifica:
1. El modelo Gemini Omni 1.1 Flash (la evolución oficial de Veo 3.1 en Google GenAI)
   para generar tomas de video vertical (9:16) mediante la Interactions API.
2. La arquitectura de edición viral de Phone Repair Guru y Wiltech (100% video real,
   cortes rápidos sincronizados, subtítulos llamativos y diseño sonoro).
=============================================================================
"""

import os
import sys
import argparse
import subprocess
from pathlib import Path
from google import genai
from google.genai import types

if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass

BASE_DIR = Path(r"C:\Users\SAmue\Desktop\Volt-Repair-Studio")
VIDEOS_DIR = BASE_DIR / "videos"
BROLL_DIR = VIDEOS_DIR / "b_roll"
EXPORT_DIR = VIDEOS_DIR / "reels_exportados"
OMNI_SCRIPT = Path(r"C:\Users\SAmue\.gemini\config\plugins\gemini-api\skills\gemini-omni-flash-api\scripts\video\generate_video.py")

PROMPTS_OMNI = [
    {
        "id": "omni_pantalla_desarmador",
        "prompt": "Cinematic vertical 9:16 macro shot of a repair technician hands using a precision magnetic screwdriver to remove bottom screws from a modern smartphone on a blue heat-resistant silicone repair mat, natural studio lighting, ultra sharp focus 4k.",
        "duration": 5,
        "aspect_ratio": "9:16",
        "resolution": "720p"
    },
    {
        "id": "omni_truetone_microscopio",
        "prompt": "Vertical 9:16 cinematic video of a phone logic board under a trinocular stereo microscope with LED ring light, micro soldering iron heating an IC chip with subtle flux smoke, high tech repair laboratory, 4k photorealistic.",
        "duration": 5,
        "aspect_ratio": "9:16",
        "resolution": "720p"
    },
    {
        "id": "omni_bateria_pulltabs",
        "prompt": "Vertical 9:16 close up of repair tweezers peeling clean stretch-release adhesive pull tabs from an OEM smartphone battery inside an opened phone chassis, spotless aluminum frame, satisfying tech repair motion, 4k.",
        "duration": 5,
        "aspect_ratio": "9:16",
        "resolution": "720p"
    }
]

def generate_omni_clip(clip_cfg: dict, output_dir: Path):
    cid = clip_cfg["id"]
    out_file = output_dir / f"{cid}.mp4"
    if out_file.exists() and out_file.stat().st_size > 1000:
        print(f"⏩ Clip {cid} ya existe ({out_file.stat().st_size / (1024*1024):.2f} MB). Saltando...")
        return out_file

    print(f"\n🚀 Generando clip con Gemini Omni Flash: '{cid}'...")
    print(f"Prompt: {clip_cfg['prompt']}")
    
    cmd = [
        sys.executable, str(OMNI_SCRIPT),
        clip_cfg["prompt"],
        "--aspect-ratio", clip_cfg["aspect_ratio"],
        "--duration", str(clip_cfg["duration"]),
        "--resolution", clip_cfg["resolution"],
        "--output", str(out_file)
    ]
    res = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", errors="ignore")
    if res.returncode == 0 and out_file.exists():
        print(f"✅ Clip generado con éxito: {out_file.name}")
        return out_file
    else:
        print(f"⚠️ Error generando {cid} con Gemini Omni API:")
        print(res.stderr[:400])
        return None

def main():
    parser = argparse.ArgumentParser(description="Generador de Reels con Veo 3.1 y Gemini Omni Flash")
    parser.add_argument("--generate-omni", action="store_true", help="Generar nuevos clips con Gemini Omni Flash API")
    parser.add_argument("--render-final", action="store_true", default=True, help="Renderizar los 3 reels finales con la arquitectura viral")
    args = parser.parse_args()

    print("==================================================================")
    print("⚡ VOLT REPAIR STUDIO — PIPELINE VEO 3.1 & GEMINI OMNI FLASH")
    print("==================================================================")

    if args.generate_omni:
        for p in PROMPTS_OMNI:
            generate_omni_clip(p, BROLL_DIR)

    if args.render_final:
        print("\n🎬 Ejecutando renderizado de alta producción (100% video real)...")
        render_script = VIDEOS_DIR / "render_viral_tech_reels.py"
        subprocess.run([sys.executable, str(render_script)], check=True)

if __name__ == "__main__":
    main()
