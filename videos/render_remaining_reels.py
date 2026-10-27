import os
import subprocess
import shutil
from pathlib import Path

BASE_DIR = Path(r"C:\Users\SAmue\Desktop\Volt-Repair-Studio")
REMOTION_DIR = BASE_DIR / "remotion_reels"
OUT_DIR = REMOTION_DIR / "out"
EXPORT_DIR = BASE_DIR / "videos" / "reels_exportados"
OUT_DIR.mkdir(parents=True, exist_ok=True)
EXPORT_DIR.mkdir(parents=True, exist_ok=True)

REELS_TO_RENDER = [
    (5, "VoltReelPuerto", "reel_05_puerto_carga_master_1080x1920.mp4"),
    (6, "VoltReelFaceID", "reel_06_face_id_master_1080x1920.mp4"),
    (7, "VoltReelCamara", "reel_07_camara_ois_master_1080x1920.mp4"),
    (8, "VoltReelMojados", "reel_08_mojados_arroz_master_1080x1920.mp4"),
]

for idx, comp_id, out_file in REELS_TO_RENDER:
    out_path = OUT_DIR / out_file
    export_path = EXPORT_DIR / out_file
    print(f"\n=======================================================", flush=True)
    print(f"[{idx}/8] RENDERIZANDO: {comp_id} -> {out_file}", flush=True)
    print(f"=======================================================", flush=True)
    
    cmd = f'npx remotion render {comp_id} out/{out_file} --concurrency=4'
    res = subprocess.run(cmd, cwd=str(REMOTION_DIR), shell=True)
    if res.returncode == 0 and out_path.exists():
        shutil.copy2(out_path, export_path)
        print(f"[OK] Exportado con exito: {export_path.name} ({export_path.stat().st_size // (1024*1024)} MB)", flush=True)
    else:
        print(f"[ERROR] Error renderizando {comp_id}", flush=True)

print("\nTodos los Reels restantes fueron renderizados y exportados exitosamente!", flush=True)
