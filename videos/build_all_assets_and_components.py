import os
import sys
import json
import time
import hashlib
import urllib.request
import urllib.parse
from pathlib import Path
from PIL import Image

BASE_DIR = Path(r"C:\Users\SAmue\Desktop\Volt-Repair-Studio")
VIDEOS_DIR = BASE_DIR / "videos"
REMOTION_DIR = BASE_DIR / "remotion_reels"
PUBLIC_DIR = REMOTION_DIR / "public"
REGISTRY_FILE = VIDEOS_DIR / "used_images_registry.json"

LOCAL_STOCK_DIR = VIDEOS_DIR / "b_roll" / "stock_repair"
ASSETS_DIR = BASE_DIR / "assets"
TARGET_W, TARGET_H = 1080, 1920

used_images = set()
if REGISTRY_FILE.exists():
    try:
        with open(REGISTRY_FILE, "r", encoding="utf-8") as f:
            used_images = set(json.load(f))
    except Exception:
        used_images = set()

def save_registry():
    with open(REGISTRY_FILE, "w", encoding="utf-8") as f:
        json.dump(sorted(list(used_images)), f, indent=2, ensure_ascii=False)

def get_hash(path):
    with open(path, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()

def crop_and_scale(src_path, dest_path):
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
        print(f"Error cropping {src_path}: {e}")
        return False

def search_wikimedia(query):
    url = (
        f"https://commons.wikimedia.org/w/api.php?action=query&generator=search"
        f"&gsrsearch={urllib.parse.quote(query)}&gsrnamespace=6&gsrlimit=10"
        f"&prop=imageinfo&iiprop=url|size|mime&iiurlwidth=1280&format=json"
    )
    req = urllib.request.Request(url, headers={"User-Agent": "VoltRepairStudio/2.0 (contact@voltrepair.mx)"})
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            pages = data.get("query", {}).get("pages", {})
            for pid, p in pages.items():
                title = p.get("title", "").lower()
                if any(bad in title for bad in ["car", "train", "ship", "rail", "church", "building", "statue"]):
                    continue
                info = p.get("imageinfo", [{}])[0]
                thumb = info.get("thumburl") or info.get("url", "")
                clean_url = thumb.split("?")[0].lower()
                if any(clean_url.endswith(ext) for ext in [".jpg", ".jpeg", ".png", ".webp"]):
                    h = hashlib.sha256(thumb.encode("utf-8")).hexdigest()
                    if h in used_images:
                        continue
                    
                    temp_p = VIDEOS_DIR / "b_roll" / f"temp_dl_{int(time.time()*1000)}.jpg"
                    temp_p.parent.mkdir(parents=True, exist_ok=True)
                    dl_req = urllib.request.Request(thumb, headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"})
                    with urllib.request.urlopen(dl_req, timeout=12) as dl_resp, open(temp_p, "wb") as f_out:
                        f_out.write(dl_resp.read())
                    
                    try:
                        with Image.open(temp_p) as test_img:
                            test_img.verify()
                        used_images.add(h)
                        save_registry()
                        return temp_p
                    except Exception:
                        if temp_p.exists():
                            temp_p.unlink()
    except Exception:
        pass
    return None

def get_unique_image(query, keywords, out_dest):
    dl_path = search_wikimedia(query)
    if dl_path and dl_path.exists():
        crop_and_scale(dl_path, out_dest)
        dl_path.unlink()
        return True

    for d in [LOCAL_STOCK_DIR, ASSETS_DIR]:
        if not d.exists():
            continue
        for f in d.iterdir():
            if f.suffix.lower() in [".jpg", ".jpeg", ".png"]:
                h = get_hash(f)
                if h not in used_images:
                    fname = f.stem.lower()
                    if any(k.lower() in fname for k in keywords):
                        used_images.add(h)
                        save_registry()
                        crop_and_scale(f, out_dest)
                        return True

    for d in [LOCAL_STOCK_DIR, ASSETS_DIR]:
        if not d.exists():
            continue
        for f in d.iterdir():
            if f.suffix.lower() in [".jpg", ".jpeg", ".png"]:
                h = get_hash(f)
                if h not in used_images:
                    used_images.add(h)
                    save_registry()
                    crop_and_scale(f, out_dest)
                    return True

    crop_and_scale(ASSETS_DIR / "logo-volt-studio.jpg", out_dest)
    return True

from generate_all_5_voices import REELS_SPEECH

DURATION_FRAMES = {
    4: 1654,
    5: 1746,
    6: 1874,
    7: 1663,
    8: 1890,
}

COMPONENT_CONFIG = {
    4: ("VoltReel4_Laser", "Tapa Trasera Máquina Láser", "#ff0055", "$500 M.O.", "Láser de Fibra Óptica"),
    5: ("VoltReel5_Puerto", "Limpieza de Puerto de Carga", "#00f0ff", "$300 M.O.", "Limpieza Antiestática de Puerto"),
    6: ("VoltReel6_FaceID", "Reparación de Face ID", "#a855f7", "$700 M.O.", "Microelectrónica Dot Projector"),
    7: ("VoltReel7_Camara", "Cámara y Estabilizador OIS", "#ffea00", "$600 M.O.", "Estabilizador OIS y Lentes 4K"),
    8: ("VoltReel8_Mojados", "Celulares Mojados vs Arroz", "#10b981", "$500 M.O.", "Desoxidación Ultrasónica 99%"),
}

for reel_id in [4, 5, 6, 7, 8]:
    scenes = REELS_SPEECH[reel_id]
    stock_folder = PUBLIC_DIR / f"stock_reel{reel_id}"
    stock_folder.mkdir(parents=True, exist_ok=True)
    comp_name, comp_title, comp_accent, comp_price, comp_subtitle = COMPONENT_CONFIG[reel_id]
    tot_frames = DURATION_FRAMES[reel_id]
    
    num_scenes = len(scenes)
    frames_per_scene = tot_frames // num_scenes
    remainder = tot_frames % num_scenes
    
    scene_configs = []
    curr_frame = 0
    print(f"\n================ REEL {reel_id}: {comp_title} ================")
    
    for idx, sc in enumerate(scenes):
        s_id, text, badge, headline, accent, kw, online_q = sc
        dur = frames_per_scene + (1 if idx < remainder else 0)
        img_name = f"{s_id}_{kw.replace(' ', '_')[:16]}.jpg"
        img_path = stock_folder / img_name
        
        get_unique_image(online_q, [kw], img_path)
        print(f"  [{idx+1:02d}/{num_scenes}] F{curr_frame:4d}-F{curr_frame+dur:4d} ({dur}f, {dur/30.0:.2f}s) -> {img_name}")
        
        scene_configs.append({
            "from": curr_frame,
            "durationInFrames": dur,
            "img": f"stock_reel{reel_id}/{img_name}",
            "badge": badge,
            "headline": headline,
            "accent": accent,
        })
        curr_frame += dur

    scenes_json = json.dumps(scene_configs, indent=2, ensure_ascii=False)
    tsx_content = f'''import React from "react";
import {{
  AbsoluteFill,
  Audio,
  Img,
  interpolate,
  Sequence,
  spring,
  staticFile,
  useCurrentFrame,
  useVideoConfig,
}} from "remotion";

interface SceneConfig {{
  from: number;
  durationInFrames: number;
  img: string;
  badge: string;
  headline: string;
  accent: string;
}}

const SCENES_REEL{reel_id}: SceneConfig[] = {scenes_json};

const SceneSlide: React.FC<{{
  scene: SceneConfig;
  index: number;
}}> = ({{ scene, index }}) => {{
  const frame = useCurrentFrame();
  const {{ fps }} = useVideoConfig();

  const scale = interpolate(
    frame,
    [0, scene.durationInFrames],
    [1.0, 1.16],
    {{ extrapolateRight: "clamp" }}
  );

  const translateY = interpolate(
    frame,
    [0, scene.durationInFrames],
    index % 2 === 0 ? [-12, 18] : [18, -12],
    {{ extrapolateRight: "clamp" }}
  );

  const fadeIn = interpolate(frame, [0, 5], [0, 1], {{
    extrapolateRight: "clamp",
  }});

  const textSpring = spring({{
    frame,
    fps,
    config: {{ damping: 140, mass: 0.55 }},
  }});

  return (
    <AbsoluteFill style={{{{ opacity: fadeIn }}}}>
      <AbsoluteFill
        style={{{{
          transform: `scale(${{scale}}) translateY(${{translateY}}px)`,
          transformOrigin: "center center",
        }}}}
      >
        <Img
          src={{staticFile(scene.img)}}
          style={{{{
            width: "100%",
            height: "100%",
            objectFit: "cover",
          }}}}
        />
      </AbsoluteFill>

      <AbsoluteFill
        style={{{{
          background:
            "linear-gradient(180deg, rgba(6, 9, 17, 0.90) 0%, rgba(6, 9, 17, 0.20) 22%, rgba(6, 9, 17, 0.25) 62%, rgba(6, 9, 17, 0.96) 100%)",
        }}}}
      />

      <div
        style={{{{
          position: "absolute",
          top: 175,
          left: 0,
          right: 0,
          display: "flex",
          justifyContent: "center",
          transform: `scale(${{interpolate(textSpring, [0, 1], [0.7, 1])}})`,
        }}}}
      >
        <div
          style={{{{
            background: scene.accent,
            color: "#050914",
            padding: "10px 28px",
            borderRadius: 30,
            fontSize: 24,
            fontWeight: 900,
            fontFamily: "Arial Black, sans-serif",
            letterSpacing: 1,
            boxShadow: `0 0 30px ${{scene.accent}}99`,
          }}}}
        >
          {{scene.badge}}
        </div>
      </div>

      <div
        style={{{{
          position: "absolute",
          top: 260,
          left: 45,
          right: 45,
          textAlign: "center",
          transform: `translateY(${{interpolate(textSpring, [0, 1], [30, 0])}}px)`,
        }}}}
      >
        <h2
          style={{{{
            fontSize: 48,
            fontWeight: 900,
            color: "#ffffff",
            textTransform: "uppercase",
            fontFamily: "Arial Black, sans-serif",
            lineHeight: 1.15,
            margin: 0,
            WebkitTextStroke: "6px #000000",
            paintOrder: "stroke fill",
            textShadow: "0 10px 35px rgba(0,0,0,0.95)",
          }}}}
        >
          {{scene.headline}}
        </h2>
      </div>
    </AbsoluteFill>
  );
}};

export const {comp_name}: React.FC = () => {{
  const frame = useCurrentFrame();
  const {{ fps, durationInFrames, width }} = useVideoConfig();

  const headerEntrance = spring({{
    frame,
    fps,
    config: {{ damping: 200, mass: 0.5 }},
  }});

  const ctaPulse = interpolate(
    Math.sin((frame / fps) * 3.5),
    [-1, 1],
    [0.985, 1.015]
  );

  const progressWidth = interpolate(frame, [0, durationInFrames], [0, width], {{
    extrapolateRight: "clamp",
  }});

  return (
    <AbsoluteFill style={{{{ backgroundColor: "#060911" }}}}>
      {{SCENES_REEL{reel_id}.map((scene, i) => (
        <Sequence
          key={{i}}
          from={{scene.from}}
          durationInFrames={{scene.durationInFrames}}
        >
          <SceneSlide scene={{scene}} index={{i}} />
        </Sequence>
      ))}}

      <div
        style={{{{
          position: "absolute",
          top: 55,
          left: 0,
          right: 0,
          display: "flex",
          justifyContent: "center",
          alignItems: "center",
          gap: 16,
          transform: `translateY(${{interpolate(headerEntrance, [0, 1], [-70, 0])}}px)`,
          opacity: headerEntrance,
        }}}}
      >
        <Img
          src={{staticFile("logo.jpg")}}
          style={{{{
            width: 68,
            height: 68,
            borderRadius: 16,
            boxShadow: "0 0 25px {comp_accent}aa",
            border: "2px solid {comp_accent}",
          }}}}
        />
        <div>
          <h1
            style={{{{
              margin: 0,
              fontSize: 38,
              fontWeight: 900,
              color: "#ffffff",
              letterSpacing: 1.5,
              fontFamily: "Arial Black, sans-serif",
            }}}}
          >
            VOLT REPAIR STUDIO
          </h1>
          <span
            style={{{{
              fontSize: 20,
              color: "{comp_accent}",
              fontWeight: 800,
              letterSpacing: 2,
              textTransform: "uppercase",
              fontFamily: "Arial, sans-serif",
            }}}}
          >
            {comp_subtitle}
          </span>
        </div>
      </div>

      <div
        style={{{{
          position: "absolute",
          bottom: 70,
          left: 45,
          right: 45,
          transform: `scale(${{ctaPulse}})`,
        }}}}
      >
        <div
          style={{{{
            background: "rgba(10, 16, 30, 0.95)",
            border: "3px solid {comp_accent}",
            borderRadius: 26,
            padding: "18px 24px",
            textAlign: "center",
            boxShadow: "0 0 35px {comp_accent}66",
            backdropFilter: "blur(14px)",
          }}}}
        >
          <div
            style={{{{
              display: "inline-flex",
              alignItems: "center",
              justifyContent: "center",
              gap: 10,
              background: "linear-gradient(135deg, {comp_accent}, #00f0ff)",
              padding: "12px 26px",
              borderRadius: 16,
              boxShadow: "0 0 20px {comp_accent}88",
              marginBottom: 10,
            }}}}
          >
            <span
              style={{{{
                fontSize: 28,
                fontWeight: 900,
                color: "#050914",
                fontFamily: "Arial Black, sans-serif",
              }}}}
            >
              📲 WhatsApp: 720 815 7790
            </span>
          </div>
          <div
            style={{{{
              display: "flex",
              justifyContent: "center",
              gap: 18,
              fontSize: 20,
              color: "#e2e8f0",
              fontWeight: 800,
              fontFamily: "Arial, sans-serif",
            }}}}
          >
            <span>🛡️ 90 Días de Garantía</span>
            <span>•</span>
            <span>📍 En tu sala en 25 min</span>
          </div>
        </div>
      </div>

      <div
        style={{{{
          position: "absolute",
          bottom: 0,
          left: 0,
          height: 14,
          width: `${{progressWidth}}px`,
          background: "linear-gradient(90deg, {comp_accent}, #00f0ff, #10b981)",
          boxShadow: "0 0 20px {comp_accent}cc",
        }}}}
      />

      <Audio src={{staticFile("volt_voice_reel{reel_id}.mp3")}} volume={{1.0}} />
      <Audio src={{staticFile("bg_music.webm")}} volume={{0.12}} loop />
    </AbsoluteFill>
  );
}};
'''
    component_file = REMOTION_DIR / "src" / "VoltReel" / f"{comp_name}.tsx"
    component_file.write_text(tsx_content, encoding="utf-8")
    print(f"Generated React component: {component_file.name}")

print("\nAll 5 Remotion components generated successfully!")
