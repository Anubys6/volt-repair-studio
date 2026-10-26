"""
=============================================================================
⚡ GENERADOR DE 3 NUEVOS REELS VIRALES — VOLT REPAIR STUDIO
=============================================================================
Metodología Anti-Slop de la Mente Colmena:
1. Reel A: "¿POR QUÉ LA GENTE LE TIENE MIEDO A LOS TALLERES?" (Transparencia en tu sala)
2. Reel B: "¿POR QUÉ EN LAS PLAZAS TE DEJAN SIN TRUETONE?" (Programación EEPROM)
3. Reel C: "ENCONTRAMOS CINTA ESCOLAR EN ESTA BATERÍA..." (Tiras térmicas OEM)
=============================================================================
"""

import os
import sys
import asyncio
import subprocess
from pathlib import Path
from typing import Dict, Any, List
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import imageio_ffmpeg
import edge_tts

if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding='utf-8')
        sys.stderr.reconfigure(encoding='utf-8')
    except Exception:
        pass

BASE_DIR = Path(r"C:\Users\SAmue\Desktop\Volt-Repair-Studio")
VIDEOS_DIR = BASE_DIR / "videos"
EXPORT_DIR = VIDEOS_DIR / "reels_exportados"
ASSETS_DIR = BASE_DIR / "assets"
EXPORT_DIR.mkdir(parents=True, exist_ok=True)

FFMPEG_EXE = imageio_ffmpeg.get_ffmpeg_exe()

FONT_TITLE_PATH = r"C:\Windows\Fonts\ariblk.ttf"
if not os.path.exists(FONT_TITLE_PATH):
    FONT_TITLE_PATH = r"C:\Windows\Fonts\arialbd.ttf"
FONT_BODY_PATH = r"C:\Windows\Fonts\arialbd.ttf"
FONT_REGULAR_PATH = r"C:\Windows\Fonts\arial.ttf"

NUEVOS_REELS = [
    {
        "id": "reel_transparencia_sala_700",
        "tema": "Transparencia Quirúrgica en tu Comedor",
        "badge": "👁️ CERO ROBO DE PIEZAS",
        "bg_image": "render-servicio-domicilio.jpg",
        "accent_color": (0, 240, 255),       # Cyan Volt
        "secondary_color": (255, 230, 0),    # Amarillo Neón
        "hook_text": "¿POR QUÉ LA GENTE TIENE MIEDO A LOS TALLERES?",
        "body_text": "Porque temen que cambien piezas originales o vean fotos privadas. En Volt reparamos frente a ti en tu sala en 25 min. Mano de obra: $700 pesos.",
        "cta_text": "📲 Mándanos WhatsApp al 720 815 7790",
        "narration": "¿Por qué la gente tiene miedo de mandar su teléfono a reparar? Porque temen que les cambien piezas originales o miren sus fotos privadas. En Volt Repair Studio vamos a tu casa y reparamos frente a ti en veinticinco minutos. Mano de obra de pantalla solo setecientos pesos. ¡Escríbenos al WhatsApp en pantalla!",
        "copy_text": (
            "👁️ ¿Por qué la gente le tiene tanto miedo a los talleres de celulares? 📱🔐\n\n"
            "El mayor temor de todos es que te roben piezas originales, te instalen pantallas de desecho o revisen tus fotos privadas. ¡En Volt Repair Studio acabamos con eso!\n\n"
            "⚡ Micro-cirugía en tu propia casa u oficina en 25 minutos\n"
            "👀 Tú estás presente viendo cada tornillo sobre tu mesa\n"
            "💰 Mano de obra fija de pantalla: Solo $700 MXN (+ refacción certificada)\n"
            "🛡️ 90 días de garantía total por escrito\n\n"
            "📲 Agenda tu cita hoy por WhatsApp: +52 1 720 815 7790\n"
            "🌐 Web Oficial: https://anubys6.github.io/volt-repair-studio/\n"
            "🎵 TikTok: https://www.tiktok.com/@voltrepair32\n\n"
            "#voltrepair32 #VoltRepairStudio #ReparacionDeCelulares #iPhoneMexico #ReparacionADomicilio #PantallaRota #ManoDeObraTransparente #SamsungMexico #TecnologiaMexico"
        )
    },
    {
        "id": "reel_truetone_programadora_700",
        "tema": "El Secreto del TrueTone y los 120Hz",
        "badge": "🔬 PROGRAMACIÓN EEPROM",
        "bg_image": "render-computadora-laboratorio.jpg",
        "accent_color": (168, 85, 247),      # Púrpura Neón
        "secondary_color": (0, 240, 255),    # Cyan
        "hook_text": "¿POR QUÉ EN LAS PLAZAS TE DEJAN SIN TRUETONE?",
        "body_text": "Porque cambian la pantalla sin programadora. Nosotros transferimos el serial original y calibramos los 120Hz ProMotion frente a ti. Mano de obra: $700 pesos.",
        "cta_text": "⚡ Agenda tu pantalla perfecta por WhatsApp",
        "narration": "¿Por qué cuando te cambian la pantalla en las plazas se pierde el brillo automático y el TrueTone? Porque no usan programadora. En Volt transferimos la memoria original de tu pantalla para que conserve todos los colores y los ciento veinte Hertz. Mano de obra de setecientos pesos. ¡Cotiza tu modelo por WhatsApp!",
        "copy_text": (
            "⚠️ ¿Te cambiaron la pantalla y perdiste el TrueTone y el brillo automático? 📉📱\n\n"
            "En muchos talleres callejeros montan pantallas genéricas sin transferir el código serial de la memoria EEPROM original. En Volt Repair Studio usamos programadora de micro-chips para calibrar tu pantalla y conservar los 120Hz ProMotion.\n\n"
            "🔬 Trabajo quirúrgico frente a ti en 25 minutos\n"
            "💰 Mano de obra de pantalla: Solo $700 MXN (+ pieza OEM Grado A+)\n"
            "🛡️ 90 días de garantía por escrito\n\n"
            "📲 Mándanos mensaje directo al WhatsApp: +52 1 720 815 7790\n"
            "🌐 Web: https://anubys6.github.io/volt-repair-studio/\n"
            "🎵 TikTok: https://www.tiktok.com/@voltrepair32\n\n"
            "#voltrepair32 #TrueTone #PantallaiPhone #CambioDePantalla #VoltRepairStudio #iPhone14Pro #MicroElectronica #ReparacionCelulares"
        )
    },
    {
        "id": "reel_bateria_cinta_escolar_500",
        "tema": "Batería Degradada y Tiras Térmicas OEM",
        "badge": "🔋 ALERTA EN LA BATERÍA",
        "bg_image": "render-taller-laboratorio.jpg",
        "accent_color": (16, 185, 129),      # Verde Neón
        "secondary_color": (255, 255, 255),
        "hook_text": "ENCONTRAMOS CINTA ESCOLAR EN ESTA BATERÍA...",
        "body_text": "Cuidado con los talleres callejeros que usan pegamento tóxico. En Volt instalamos celdas certificadas con tiras térmicas elásticas de fábrica. Mano de obra: $500 pesos.",
        "cta_text": "🔋 Salud de batería al 100% al 720 815 7790",
        "narration": "¡Mira lo que encontramos adentro de este celular! Pegamento corriente en la batería que casi perfora la celda. En Volt Repair Studio instalamos baterías certificadas de alta densidad con tiras elásticas de fábrica. Mano de obra de solo quinientos pesos. ¡Recupera el cien por ciento de salud hoy escribiéndonos al WhatsApp!",
        "copy_text": (
            "🚨 ¡Cuidado con cómo te cambian la batería en la calle! 💥🔋\n\n"
            "Abrimos este equipo y encontramos cinta doble cara escolar que sobrecalienta el procesador. En Volt Repair Studio instalamos celdas de alta densidad con adhesivos térmicos elásticos pull-tabs de fábrica.\n\n"
            "⚡ Recupera la salud de tu batería al 100% en 20 minutos en tu mesa\n"
            "💰 Mano de obra garantizada: Solo $500 MXN (+ batería certificada)\n"
            "🛡️ 90 días de garantía total\n\n"
            "📲 Escríbenos por WhatsApp para cotizar tu modelo: +52 1 720 815 7790\n"
            "🌐 https://anubys6.github.io/volt-repair-studio/\n"
            "🎵 TikTok: https://www.tiktok.com/@voltrepair32\n\n"
            "#voltrepair32 #BateriaiPhone #BateriaSamsung #SaludDeBateria #VoltRepairStudio #ReparacionADomicilio #TecnologiaMexico"
        )
    }
]

def wrap_text(text: str, font: ImageFont.FreeTypeFont, max_width: int, draw: ImageDraw.ImageDraw) -> List[str]:
    words = text.split()
    lines = []
    current_line = []
    for word in words:
        test_line = " ".join(current_line + [word])
        bbox = draw.textbbox((0, 0), test_line, font=font)
        w = bbox[2] - bbox[0]
        if w <= max_width:
            current_line.append(word)
        else:
            if current_line:
                lines.append(" ".join(current_line))
            current_line = [word]
    if current_line:
        lines.append(" ".join(current_line))
    return lines

def create_card_image(
    badge: str,
    main_title: str,
    subtitle: str,
    cta: str,
    accent_color: tuple,
    secondary_color: tuple,
    bg_image_name: str,
    output_path: Path,
    stage: int = 1
):
    width, height = 1080, 1920
    base_img = Image.new("RGB", (width, height), color=(6, 9, 17))
    
    bg_path = ASSETS_DIR / bg_image_name
    if bg_path.exists():
        try:
            bg = Image.open(str(bg_path)).convert("RGB")
            ratio = max(width / bg.width, height / bg.height)
            new_w, new_h = int(bg.width * ratio), int(bg.height * ratio)
            bg = bg.resize((new_w, new_h), Image.Resampling.LANCZOS)
            crop_x = (new_w - width) // 2
            crop_y = (new_h - height) // 2
            bg = bg.crop((crop_x, crop_y, crop_x + width, crop_y + height))
            bg = bg.filter(ImageFilter.GaussianBlur(radius=16))
            darkener = Image.new("RGB", (width, height), (6, 9, 17))
            base_img = Image.blend(darkener, bg, alpha=0.32)
        except Exception:
            pass

    draw = ImageDraw.Draw(base_img)

    for y in range(0, 420):
        factor = (1 - (y / 420)) * 0.45
        draw.line([(0, y), (width, y)], fill=(int(accent_color[0] * factor), int(accent_color[1] * factor), int(accent_color[2] * factor)))

    font_badge = ImageFont.truetype(FONT_TITLE_PATH, 40)
    font_main = ImageFont.truetype(FONT_TITLE_PATH, 70)
    font_body = ImageFont.truetype(FONT_BODY_PATH, 46)
    font_cta = ImageFont.truetype(FONT_BODY_PATH, 42)
    font_brand = ImageFont.truetype(FONT_TITLE_PATH, 34)

    # 1. Cabecera oficial
    draw.text((width // 2, 130), "⚡ VOLT REPAIR STUDIO ⚡", font=font_brand, fill=(148, 163, 184), anchor="mm")
    draw.line([(width // 2 - 180, 160), (width // 2 + 180, 160)], fill=(0, 240, 255), width=2)

    # 2. Badge de choque
    badge_bbox = draw.textbbox((0, 0), badge, font=font_badge)
    bw = badge_bbox[2] - badge_bbox[0] + 60
    bh = badge_bbox[3] - badge_bbox[1] + 28
    bx1 = (width - bw) // 2
    by1 = 230
    draw.rounded_rectangle([bx1, by1, bx1 + bw, by1 + bh], radius=24, fill=accent_color)
    draw.text((width // 2, by1 + bh // 2), badge, font=font_badge, fill=(255, 255, 255), anchor="mm")

    # 3. Título principal
    title_lines = wrap_text(main_title, font_main, width - 140, draw)
    start_y = 440
    for line in title_lines:
        bbox = draw.textbbox((0, 0), line, font=font_main)
        lw = bbox[2] - bbox[0]
        lx = (width - lw) // 2
        draw.text((lx + 4, start_y + 4), line, font=font_main, fill=(0, 0, 0))
        text_color = secondary_color if stage == 1 else (255, 255, 255)
        draw.text((lx, start_y), line, font=font_main, fill=text_color)
        start_y += 88

    # 4. Divisor neón
    draw.line([(180, start_y + 35), (width - 180, start_y + 35)], fill=accent_color, width=5)
    draw.ellipse([(width // 2 - 8, start_y + 29), (width // 2 + 8, start_y + 45)], fill=(255, 255, 255))
    start_y += 90

    # 5. Cuerpo de explicación y precio
    body_lines = wrap_text(subtitle, font_body, width - 160, draw)
    for line in body_lines:
        bbox = draw.textbbox((0, 0), line, font=font_body)
        lw = bbox[2] - bbox[0]
        lx = (width - lw) // 2
        draw.text((lx + 3, start_y + 3), line, font=font_body, fill=(0, 0, 0))
        text_color = (255, 255, 255) if stage != 2 else secondary_color
        draw.text((lx, start_y), line, font=font_body, fill=text_color)
        start_y += 68

    # 6. Tarjeta de WhatsApp y CTA
    cta_box_y1 = 1500
    cta_box_y2 = 1690
    draw.rounded_rectangle([90, cta_box_y1, width - 90, cta_box_y2], radius=28, fill=(15, 23, 42), outline=accent_color, width=4)
    
    cta_lines = wrap_text(cta, font_cta, width - 220, draw)
    cy = cta_box_y1 + 45
    for line in cta_lines:
        draw.text((width // 2, cy), line, font=font_cta, fill=(255, 255, 255), anchor="mm")
        cy += 58

    # 7. Barra de progreso animada
    progress_y = height - 50
    draw.line([(60, progress_y), (width - 60, progress_y)], fill=(30, 41, 59), width=10)
    fill_ratio = stage / 3.0
    fill_w = int(60 + (width - 120) * fill_ratio)
    draw.line([(60, progress_y), (fill_w, progress_y)], fill=accent_color, width=10)

    base_img.save(str(output_path), quality=95)

async def synthesize_voice(text: str, output_path: Path):
    for attempt in range(1, 4):
        try:
            communicate = edge_tts.Communicate(
                text=text,
                voice="es-MX-JorgeNeural",
                rate="+6%",
                pitch="+0Hz"
            )
            await communicate.save(str(output_path))
            return
        except Exception as e:
            if attempt == 3:
                raise e
            await asyncio.sleep(1.5)

def build_reel_video(reel_data: Dict[str, Any]) -> Dict[str, Any]:
    reel_id = reel_data["id"]
    temp_dir = EXPORT_DIR / f"temp_{reel_id}"
    temp_dir.mkdir(parents=True, exist_ok=True)

    audio_file = temp_dir / f"{reel_id}.mp3"
    card1_file = temp_dir / "card1.png"
    card2_file = temp_dir / "card2.png"
    card3_file = temp_dir / "card3.png"
    concat_file = temp_dir / "concat.txt"
    final_video = EXPORT_DIR / f"{reel_id}_1080x1920.mp4"

    print(f"   [+] Generando locución neural mexicana (Edge-TTS)...")
    asyncio.run(synthesize_voice(reel_data["narration"], audio_file))

    dur_cmd = [
        FFMPEG_EXE, "-i", str(audio_file),
        "-show_entries", "format=duration",
        "-v", "quiet", "-of", "csv=p=0"
    ]
    try:
        dur_res = subprocess.run(dur_cmd, capture_output=True, text=True)
        audio_dur = float(dur_res.stdout.strip())
    except Exception:
        audio_dur = 14.8

    print(f"   [+] Renderizando frames 9:16 de 1080x1920 con badges neón...")
    create_card_image(
        badge=reel_data["badge"],
        main_title=reel_data["hook_text"],
        subtitle=reel_data["body_text"],
        cta=reel_data["cta_text"],
        accent_color=reel_data["accent_color"],
        secondary_color=reel_data["secondary_color"],
        bg_image_name=reel_data["bg_image"],
        output_path=card1_file,
        stage=1
    )
    create_card_image(
        badge=reel_data["badge"],
        main_title=reel_data["hook_text"],
        subtitle=reel_data["body_text"],
        cta=reel_data["cta_text"],
        accent_color=reel_data["accent_color"],
        secondary_color=reel_data["secondary_color"],
        bg_image_name=reel_data["bg_image"],
        output_path=card2_file,
        stage=2
    )
    create_card_image(
        badge="📲 CONTACTO DIRECTO",
        main_title=reel_data["hook_text"],
        subtitle="Reparaciones activas a domicilio con 90 días de garantía.",
        cta=reel_data["cta_text"],
        accent_color=reel_data["accent_color"],
        secondary_color=(255, 230, 0),
        bg_image_name=reel_data["bg_image"],
        output_path=card3_file,
        stage=3
    )

    t1 = round(audio_dur * 0.30, 2)
    t2 = round(audio_dur * 0.45, 2)
    t3 = round(audio_dur - t1 - t2, 2)

    with open(concat_file, "w", encoding="utf-8") as f:
        f.write(f"file '{card1_file.name}'\n")
        f.write(f"duration {t1}\n")
        f.write(f"file '{card2_file.name}'\n")
        f.write(f"duration {t2}\n")
        f.write(f"file '{card3_file.name}'\n")
        f.write(f"duration {t3}\n")
        f.write(f"file '{card3_file.name}'\n")

    print(f"   [+] Codificando con FFmpeg ({audio_dur:.1f}s)...")
    cmd = [
        FFMPEG_EXE, "-y",
        "-f", "concat", "-safe", "0", "-i", str(concat_file),
        "-i", str(audio_file),
        "-vf", "fps=30,format=yuv420p",
        "-c:v", "libx264",
        "-preset", "veryfast",
        "-c:a", "aac",
        "-b:a", "192k",
        "-shortest",
        str(final_video)
    ]
    res = subprocess.run(cmd, cwd=str(temp_dir), capture_output=True, text=True)
    if res.returncode != 0:
        raise RuntimeError(f"Error FFmpeg: {res.stderr}")

    copy_file = EXPORT_DIR / f"{reel_id}_texto_redes.txt"
    with open(copy_file, "w", encoding="utf-8") as f:
        f.write("=== TEXTO LISTO PARA PUBLICAR EN TIKTOK, INSTAGRAM O FACEBOOK ===\n\n")
        f.write(reel_data["copy_text"])

    print(f"   [✓] Video generado: {final_video.name}")
    print(f"   [✓] Texto listo: {copy_file.name}")

    return {
        "video": final_video,
        "copy": copy_file,
        "duration": audio_dur
    }

def main():
    print("=" * 80)
    print(" 🚀 GENERANDO 3 REELS VIRALES INMEDIATOS PARA SAMUEL")
    print("    Destino: TikTok (@voltrepair32), Instagram (@voltrepair.mx) y Facebook")
    print("=" * 80)
    
    generated = []
    for idx, reel in enumerate(NUEVOS_REELS, start=1):
        print(f"\n🎬 Procesando Reel [{idx}/3]: {reel['tema']} -> '{reel['hook_text']}'")
        try:
            res = build_reel_video(reel)
            generated.append(res)
        except Exception as e:
            print(f"   ❌ Error generando {reel['id']}: {e}")

    # Limpiar temporales
    for reel in NUEVOS_REELS:
        t_dir = EXPORT_DIR / f"temp_{reel['id']}"
        if t_dir.exists():
            for f in t_dir.iterdir():
                try: f.unlink()
                except Exception: pass
            try: t_dir.rmdir()
            except Exception: pass

    print("\n" + "=" * 80)
    print(f" ✨ ¡LOS 3 REELS ESTÁN LISTOS! Se exportaron con éxito en:")
    print(f" 📁 {EXPORT_DIR}")
    print("=" * 80)

if __name__ == "__main__":
    main()
