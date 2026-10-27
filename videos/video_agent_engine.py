import os
import sys
import json
import time
import asyncio
import hashlib
import urllib.request
import urllib.parse
import subprocess
from pathlib import Path
from PIL import Image
import edge_tts
import imageio_ffmpeg

BASE_DIR = Path(r"C:\Users\SAmue\Desktop\Volt-Repair-Studio")
VIDEOS_DIR = BASE_DIR / "videos"
REMOTION_DIR = BASE_DIR / "remotion_reels"
PUBLIC_DIR = REMOTION_DIR / "public"
EXPORT_DIR = VIDEOS_DIR / "reels_exportados"
REGISTRY_FILE = VIDEOS_DIR / "used_images_registry.json"

LOCAL_STOCK_DIR = VIDEOS_DIR / "b_roll" / "stock_repair"
ASSETS_DIR = BASE_DIR / "assets"

TARGET_W, TARGET_H = 1080, 1920

class VideoAgentEngine:
    def __init__(self):
        self.used_images = self._load_registry()
        self.ffmpeg = imageio_ffmpeg.get_ffmpeg_exe()

    def _load_registry(self):
        if REGISTRY_FILE.exists():
            try:
                with open(REGISTRY_FILE, "r", encoding="utf-8") as f:
                    return set(json.load(f))
            except Exception:
                return set()
        return set()

    def _save_registry(self):
        with open(REGISTRY_FILE, "w", encoding="utf-8") as f:
            json.dump(sorted(list(self.used_images)), f, indent=2, ensure_ascii=False)

    def _get_image_hash(self, img_path):
        with open(img_path, "rb") as f:
            return hashlib.sha256(f.read()).hexdigest()

    def crop_and_scale(self, src_path, dest_path):
        """Recorta y escala la imagen a exactamente 1080x1920 (9:16) con antialiasing Lanczos."""
        try:
            with Image.open(src_path) as img:
                img = img.convert("RGB")
                src_w, src_h = img.size
                target_ratio = TARGET_W / TARGET_H
                src_ratio = src_w / src_h

                if src_ratio > target_ratio:
                    new_w = int(src_h * target_ratio)
                    offset_x = (src_w - new_w) // 2
                    img_cropped = img.crop((offset_x, 0, offset_x + new_w, src_h))
                else:
                    new_h = int(src_w / target_ratio)
                    offset_y = (src_h - new_h) // 2
                    img_cropped = img.crop((0, offset_y, src_w, offset_y + new_h))

                img_resized = img_cropped.resize((TARGET_W, TARGET_H), Image.Resampling.LANCZOS)
                dest_path.parent.mkdir(parents=True, exist_ok=True)
                img_resized.save(dest_path, quality=92)
                return True
        except Exception as e:
            print(f"   [Error Crop] {src_path}: {e}")
            return False

    def search_local(self, keywords):
        """Busca en el repositorio local de fotografías técnicas no usadas."""
        candidates = []
        for d in [LOCAL_STOCK_DIR, ASSETS_DIR]:
            if not d.exists():
                continue
            for f in d.iterdir():
                if f.suffix.lower() in [".jpg", ".jpeg", ".png", ".webp"]:
                    h = self._get_image_hash(f)
                    if h in self.used_images:
                        continue
                    fname_lower = f.stem.lower()
                    score = sum(1 for kw in keywords if kw.lower() in fname_lower)
                    candidates.append((score, f, h))

        candidates.sort(key=lambda x: x[0], reverse=True)
        if candidates and candidates[0][0] > 0:
            best = candidates[0]
            self.used_images.add(best[2])
            self._save_registry()
            return best[1]
        return None

    def search_online_wikimedia(self, query):
        """Busca y descarga imágenes en Wikimedia Commons API a 1280px con control de deduplicación."""
        url = (
            f"https://commons.wikimedia.org/w/api.php?action=query&generator=search"
            f"&gsrsearch={urllib.parse.quote(query)}&gsrnamespace=6&gsrlimit=8"
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
                    thumb = info.get("thumburl") or info.get("url", "")
                    clean_url = thumb.split("?")[0].lower()
                    if any(clean_url.endswith(ext) for ext in [".jpg", ".jpeg", ".png", ".webp"]):
                        url_hash = hashlib.sha256(thumb.encode("utf-8")).hexdigest()
                        if url_hash in self.used_images:
                            continue
                        
                        # Descargar temporal y validar
                        temp_dest = VIDEOS_DIR / "b_roll" / f"temp_{int(time.time()*1000)}.jpg"
                        temp_dest.parent.mkdir(parents=True, exist_ok=True)
                        dl_req = urllib.request.Request(thumb, headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"})
                        with urllib.request.urlopen(dl_req, timeout=12) as dl_resp, open(temp_dest, "wb") as f_out:
                            f_out.write(dl_resp.read())
                        
                        try:
                            with Image.open(temp_dest) as img_test:
                                img_test.verify()
                            self.used_images.add(url_hash)
                            self._save_registry()
                            return temp_dest
                        except Exception:
                            if temp_dest.exists():
                                temp_dest.unlink()
        except Exception as e:
            pass
        return None

    def get_image_for_concept(self, keywords, online_query, dest_file):
        """Busca imagen para un concepto: 1) Local no usado -> 2) Wikimedia Commons -> 3) Fallback."""
        img_src = self.search_local(keywords)
        if not img_src:
            img_src = self.search_online_wikimedia(online_query)
        
        if img_src and img_src.exists():
            success = self.crop_and_scale(img_src, dest_file)
            if img_src.name.startswith("temp_"):
                img_src.unlink()
            if success:
                return dest_file

        # Fallback a local cualquiera que no esté en used_images
        for d in [LOCAL_STOCK_DIR, ASSETS_DIR]:
            if not d.exists():
                continue
            for f in d.iterdir():
                if f.suffix.lower() in [".jpg", ".jpeg", ".png"]:
                    h = self._get_image_hash(f)
                    if h not in self.used_images:
                        self.used_images.add(h)
                        self._save_registry()
                        self.crop_and_scale(f, dest_file)
                        return dest_file
        
        # Último recurso
        default_img = ASSETS_DIR / "logo-volt-studio.jpg"
        self.crop_and_scale(default_img, dest_file)
        return dest_file

    async def generate_voice(self, full_text, output_audio_path):
        """Sintetiza la voz mexicana amistosa Alonso Neural con extracción de SentenceBoundary."""
        c = edge_tts.Communicate(full_text, "es-US-AlonsoNeural", rate="+10%")
        boundaries = []
        with open(output_audio_path, "wb") as f:
            async for chunk in c.stream():
                if chunk["type"] == "audio":
                    f.write(chunk["data"])
                elif chunk["type"] == "SentenceBoundary":
                    boundaries.append(chunk)

        # Medir duración exacta con FFmpeg
        res = subprocess.run([self.ffmpeg, "-i", str(output_audio_path)], stderr=subprocess.PIPE, text=True)
        total_dur = 0.0
        for line in res.stderr.splitlines():
            if "Duration:" in line:
                parts = line.split("Duration:")[1].split(",")[0].strip().split(":")
                total_dur = float(parts[0])*3600 + float(parts[1])*60 + float(parts[2])
                break

        return boundaries, total_dur
