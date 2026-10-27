from PIL import Image
from pathlib import Path
import os

BASE_DIR = Path(r"C:\Users\SAmue\Desktop\Volt-Repair-Studio")
STOCK_DIR = BASE_DIR / "videos" / "b_roll" / "stock_repair"
ASSETS_DIR = BASE_DIR / "assets"
OUT_DIR = BASE_DIR / "remotion_reels" / "public" / "stock_congruent"
OUT_DIR.mkdir(parents=True, exist_ok=True)

# 17 Congruent Image Mappings
IMAGE_MAP = {
    "scene_01_intro.jpg": ASSETS_DIR / "render-servicio-domicilio.jpg",
    "scene_02_broken.jpg": STOCK_DIR / "repair_stock_01.jpg",
    "scene_03a_plaza.jpg": STOCK_DIR / "repair_stock_02.jpg",
    "scene_03b_privacy.jpg": STOCK_DIR / "tech_stock_28.jpg",
    "scene_04_arrival.jpg": ASSETS_DIR / "foto-real-domicilio.jpg",
    "scene_05a_dining.jpg": ASSETS_DIR / "volt_tech_living_room.jpg",
    "scene_05b_live.jpg": STOCK_DIR / "tech_stock_22.jpg",
    "scene_06_pentalobe.jpg": STOCK_DIR / "tech_stock_02.jpg",
    "scene_07_suction.jpg": STOCK_DIR / "tech_stock_03.jpg",
    "scene_08_battery.jpg": STOCK_DIR / "tech_stock_05.jpg",
    "scene_09a_truetone.jpg": ASSETS_DIR / "volt_tech_lab_truetone.jpg",
    "scene_09b_eeprom.jpg": STOCK_DIR / "tech_stock_07.jpg",
    "scene_10_new_display.jpg": STOCK_DIR / "tech_stock_08.jpg",
    "scene_11_touch_test.jpg": STOCK_DIR / "tech_stock_09.jpg",
    "scene_12a_pricing.jpg": STOCK_DIR / "tech_stock_10.jpg",
    "scene_12b_warranty.jpg": STOCK_DIR / "tech_stock_14.jpg",
    "scene_13_whatsapp.jpg": ASSETS_DIR / "logo-volt-studio.jpg",
}

TARGET_W, TARGET_H = 1080, 1920

for target_name, src_path in IMAGE_MAP.items():
    if not src_path.exists():
        print(f"WARNING: Missing {src_path}")
        continue
    
    img = Image.open(src_path).convert("RGB")
    src_w, src_h = img.size
    
    # Calculate crop to maintain 9:16 aspect ratio without distortion
    target_ratio = TARGET_W / TARGET_H
    src_ratio = src_w / src_h
    
    if src_ratio > target_ratio:
        # Source is wider: crop width
        new_w = int(src_h * target_ratio)
        offset_x = (src_w - new_w) // 2
        img_cropped = img.crop((offset_x, 0, offset_x + new_w, src_h))
    else:
        # Source is taller: crop height
        new_h = int(src_w / target_ratio)
        offset_y = (src_h - new_h) // 2
        img_cropped = img.crop((0, offset_y, src_w, offset_y + new_h))
        
    img_resized = img_cropped.resize((TARGET_W, TARGET_H), Image.Resampling.LANCZOS)
    out_file = OUT_DIR / target_name
    img_resized.save(out_file, quality=92)
    print(f"Created: {target_name} ({TARGET_W}x{TARGET_H}) from {src_path.name}")

print("\nAll 17 congruent scenes formatted perfectly!")
