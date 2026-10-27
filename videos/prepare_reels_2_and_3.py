from PIL import Image
from pathlib import Path

BASE_DIR = Path(r"C:\Users\SAmue\Desktop\Volt-Repair-Studio")
STOCK_DIR = BASE_DIR / "videos" / "b_roll" / "stock_repair"
ASSETS_DIR = BASE_DIR / "assets"
PUBLIC_DIR = BASE_DIR / "remotion_reels" / "public"

REEL2_DIR = PUBLIC_DIR / "stock_reel2"
REEL3_DIR = PUBLIC_DIR / "stock_reel3"
REEL2_DIR.mkdir(parents=True, exist_ok=True)
REEL3_DIR.mkdir(parents=True, exist_ok=True)

TARGET_W, TARGET_H = 1080, 1920

def crop_and_save(src_path, out_file):
    img = Image.open(src_path).convert("RGB")
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
    img_resized.save(out_file, quality=92)
    print(f"Saved: {out_file.name} from {src_path.name}")

# Reel 2 Images
REEL2_MAP = {
    "scene_01_intro.jpg": ASSETS_DIR / "render-servicio-domicilio.jpg",
    "scene_02a_truetone_lost.jpg": STOCK_DIR / "repair_stock_01.jpg",
    "scene_02b_bad_shop.jpg": STOCK_DIR / "repair_stock_02.jpg",
    "scene_03_sensor_glitch.jpg": STOCK_DIR / "tech_stock_28.jpg",
    "scene_04a_eeprom_chip.jpg": STOCK_DIR / "tech_stock_27.jpg",
    "scene_04b_display_serial.jpg": STOCK_DIR / "tech_stock_07.jpg",
    "scene_05_lab_level.jpg": ASSETS_DIR / "render-equipo-microsoldadura.jpg",
    "scene_06_jcid_tool.jpg": ASSETS_DIR / "volt_tech_lab_truetone.jpg",
    "scene_07a_connect_old.jpg": STOCK_DIR / "tech_stock_06.jpg",
    "scene_07b_extract_serial.jpg": ASSETS_DIR / "render-camara-termica.jpg",
    "scene_08_write_new.jpg": STOCK_DIR / "tech_stock_08.jpg",
    "scene_09_vivid_120hz.jpg": STOCK_DIR / "tech_stock_09.jpg",
    "scene_10_live_dining.jpg": ASSETS_DIR / "volt_tech_living_room.jpg",
    "scene_11a_price700.jpg": STOCK_DIR / "tech_stock_10.jpg",
    "scene_11b_warranty.jpg": STOCK_DIR / "tech_stock_14.jpg",
    "scene_12_whatsapp.jpg": ASSETS_DIR / "logo-volt-studio.jpg",
}

print("=== Cropping Reel 2 Images ===")
for name, p in REEL2_MAP.items():
    crop_and_save(p, REEL2_DIR / name)

# Reel 3 Images
REEL3_MAP = {
    "scene_01_intro.jpg": ASSETS_DIR / "render-servicio-domicilio.jpg",
    "scene_02a_street_danger.jpg": STOCK_DIR / "tech_stock_23.jpg",
    "scene_02b_bad_kiosk.jpg": STOCK_DIR / "repair_stock_02.jpg",
    "scene_03a_draining.jpg": STOCK_DIR / "tech_stock_24.jpg",
    "scene_03b_overheating.jpg": ASSETS_DIR / "render-camara-termica.jpg",
    "scene_04a_school_tape.jpg": STOCK_DIR / "tech_stock_25.jpg",
    "scene_04b_scraped_glue.jpg": STOCK_DIR / "tech_stock_26.jpg",
    "scene_05_deformed_cell.jpg": STOCK_DIR / "tech_stock_27.jpg",
    "scene_06_factory_standard.jpg": ASSETS_DIR / "render-equipo-microsoldadura.jpg",
    "scene_07_dining_repair.jpg": ASSETS_DIR / "volt_tech_living_room.jpg",
    "scene_08_safe_disconnect.jpg": STOCK_DIR / "tech_stock_05.jpg",
    "scene_09a_pulltabs.jpg": ASSETS_DIR / "volt_tech_battery_pulltabs.jpg",
    "scene_09b_new_cell.jpg": STOCK_DIR / "tech_stock_11.jpg",
    "scene_10_health100.jpg": STOCK_DIR / "tech_stock_10.jpg",
    "scene_11a_price500.jpg": STOCK_DIR / "tech_stock_12.jpg",
    "scene_11b_warranty.jpg": STOCK_DIR / "tech_stock_14.jpg",
    "scene_12_whatsapp.jpg": ASSETS_DIR / "logo-volt-studio.jpg",
}

print("\n=== Cropping Reel 3 Images ===")
for name, p in REEL3_MAP.items():
    crop_and_save(p, REEL3_DIR / name)

print("\nAll images for Reel 2 and Reel 3 processed perfectly!")
