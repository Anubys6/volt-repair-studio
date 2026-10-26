"""
=============================================================================
⚡ GENERADOR DE REELS / TIKTOKS AUTOMÁTICO — VOLT REPAIR STUDIO
=============================================================================
Arquitectura Anti-Slop de Alto Impacto inspirada en la Mente Colmena:
- Relación de aspecto 9:16 vertical (1080 x 1920).
- Duración quirúrgica de 14-16 segundos para máxima retención algorítmica.
- Locución neural de alta fidelidad en español de México (es-MX-JorgeNeural).
- Tarjetas visuales de alto contraste con badges cyberpunk y assets oficiales.
- Exportación directa de video MP4 + archivo TXT con copy para Reels y TikTok.
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

# Forzar codificación UTF-8 en consola de Windows
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding='utf-8')
        sys.stderr.reconfigure(encoding='utf-8')
    except Exception:
        pass

BASE_DIR = Path(__file__).resolve().parent.parent
VIDEOS_DIR = BASE_DIR / "videos"
EXPORT_DIR = VIDEOS_DIR / "reels_exportados"
ASSETS_DIR = BASE_DIR / "assets"
EXPORT_DIR.mkdir(parents=True, exist_ok=True)

FFMPEG_EXE = imageio_ffmpeg.get_ffmpeg_exe()

# Fuentes de Windows
FONT_TITLE_PATH = r"C:\Windows\Fonts\ariblk.ttf"
if not os.path.exists(FONT_TITLE_PATH):
    FONT_TITLE_PATH = r"C:\Windows\Fonts\arialbd.ttf"
FONT_BODY_PATH = r"C:\Windows\Fonts\arialbd.ttf"
FONT_REGULAR_PATH = r"C:\Windows\Fonts\arial.ttf"

# Datos Oficiales de los Reels de Volt Repair Studio
REELS_DATA = [
    {
        "id": "reel_01_pantalla_domicilio",
        "tema": "Pantallas iPhone y Android",
        "badge": "⚡ CIRUGÍA EN TU SALA",
        "bg_image": "foto-real-domicilio.jpg",
        "accent_color": (0, 240, 255),      # Cyan Volt
        "secondary_color": (255, 230, 0),   # Amarillo Neón
        "hook_text": "¿PANTALLA ROTA? LA CAMBIAMOS FRENTE A TI",
        "body_text": "Mano de obra fija: $700 pesos. Cero copias de tus fotos o contraseñas. Reparación en 25 minutos sobre tu mesa.",
        "cta_text": "📲 Cotiza por WhatsApp al 720 815 7790",
        "narration": "¿Pantalla estrellada en tu iPhone o Android? Te cobramos solo setecientos pesos de mano de obra y la cambiamos en veinticinco minutos frente a tus ojos en tu propia casa u oficina. Cero miedo a que toquen tus fotos. ¡Mándanos un WhatsApp al número en pantalla!",
        "copy_text": (
            "⚡ ¿Pantalla estrellada? No la dejes en un taller desconocido 📱🛠️\n\n"
            "En Volt Repair Studio vamos hasta tu casa u oficina y cambiamos la pantalla de tu iPhone, Samsung, Motorola o Xiaomi FRENTE A TI en 25 minutos.\n\n"
            "💰 Mano de obra garantizada: Solo $700 MXN (+ refacción certificada)\n"
            "🔒 Cero acceso a tus contraseñas ni a tu galería privada\n"
            "🛡️ 90 días de garantía por escrito\n\n"
            "📲 Agenda tu visita hoy mismo por WhatsApp: +52 1 720 815 7790\n"
            "🌐 Visita: https://anubys6.github.io/volt-repair-studio/\n\n"
            "#VoltRepair #ReparacionDeCelulares #iPhoneMexico #ReparacionADomicilio #PantallaRota #ManoDeObraTransparente #TikTokTech"
        )
    },
    {
        "id": "reel_02_bateria_salud100",
        "tema": "Baterías de Alta Densidad",
        "badge": "🔋 CERO CINTA ESCOLAR",
        "bg_image": "render-equipo-microsoldadura.jpg",
        "accent_color": (16, 185, 129),    # Verde Volt
        "secondary_color": (255, 255, 255),
        "hook_text": "BATERÍA AL 100% CON ADHESIVOS OEM",
        "body_text": "Mano de obra: $500 pesos. Reemplazamos celdas degradadas usando tiras térmicas elásticas pull-tab de fábrica.",
        "cta_text": "⚡ Agenda tu cambio express por WhatsApp",
        "narration": "¿Tu celular se apaga al veinte por ciento? No aceptes que le pongan cinta doble cara corriente. En Volt instalamos celdas de alta densidad con tiras elásticas de fábrica. Mano de obra de solo quinientos pesos. ¡Escríbenos al WhatsApp y revive tu batería hoy!",
        "copy_text": (
            "🔋 ¿Tu celular ya no llega a la tarde o se apaga al 20%? ⚠️\n\n"
            "Desenmascaramos el cambio callejero: muchos talleres usan cinta de doble cara escolar que arruina el chasis. En Volt Repair Studio usamos tiras elásticas térmicas OEM de grado de fábrica.\n\n"
            "💰 Mano de obra: $500 MXN (+ batería certificada)\n"
            "⚡ Salud de batería al 100% en 20 minutos en tu mesa\n"
            "🛡️ 90 días de garantía total\n\n"
            "📲 Mándanos mensaje directo al WhatsApp: +52 1 720 815 7790\n"
            "🌐 Web: https://anubys6.github.io/volt-repair-studio/\n\n"
            "#BateriaiPhone #CambioDeBateria #VoltRepairStudio #Tecnologia #TrucosCelulares #ReparacionExpress"
        )
    },
    {
        "id": "reel_03_cero_mojados_verdad",
        "tema": "Política de Honestidad Técnica",
        "badge": "🚫 LA VERDAD DEL ARROZ",
        "bg_image": "render-camara-termica.jpg",
        "accent_color": (239, 68, 68),     # Rojo Alerta
        "secondary_color": (255, 215, 0),   # Dorado
        "hook_text": "POR QUÉ NO REPARAMOS CELULARES MOJADOS",
        "body_text": "El arroz y las tinas ultrasónicas no curan la corrosión galvánica. Te decimos la verdad científica sin cobrarte falsas esperanzas.",
        "cta_text": "🔬 Diagnóstico ético en Volt Repair Studio",
        "narration": "¿Se te cayó el celular a la alberca y te dijeron que lo metieras en arroz? ¡Es una mentira! En Volt Repair Studio NO aceptamos equipos mojados porque la corrosión galvánica destruye las pistas internas. Preferimos decirte la verdad antes de cobrarte por una tina inútil.",
        "copy_text": (
            "⚠️ ¿Por qué en Volt Repair Studio NO aceptamos celulares caídos al agua? 🌊🚫\n\n"
            "Muchos talleres te cobran por meter tu equipo a una 'tina de ultrasonido' o te dicen que el arroz lo salva. La verdad científica es que el agua mineralizada provoca corrosión galvánica instantánea en las pistas de cobre.\n\n"
            "💡 Nuestra filosofía es la honestidad médica total: no te cobramos falsas esperanzas por un equipo sentenciado.\n\n"
            "📲 Si tu equipo tiene falla de pantalla, batería o tapa trasera, agenda con nosotros: +52 1 720 815 7790\n"
            "🌐 https://anubys6.github.io/volt-repair-studio/\n\n"
            "#CelularesMojados #VerdadTecnica #IngenieriaReal #VoltRepair #Honestidad #Antiestafa"
        )
    },
    {
        "id": "reel_04_tapa_trasera_laser",
        "tema": "Micro-Láser para Tapas Traseras",
        "badge": "💎 CRISTAL TRASERO IMPECABLE",
        "bg_image": "render-maquina-laser.jpg",
        "accent_color": (168, 85, 247),   # Púrpura Neón
        "secondary_color": (0, 240, 255),  # Cyan
        "hook_text": "TAPA TRASERA DE CRISTAL SIN DESARMAR",
        "body_text": "Mano de obra: $500 pesos. Desintegración de epóxico con máquina láser quirúrgica protegiendo la carga MagSafe.",
        "cta_text": "⚡ Haz que tu iPhone luzca como nuevo hoy",
        "narration": "¿Tu tapa trasera parece telaraña? Olvídate de los cinceles que dañan la carga inalámbrica. En Volt utilizamos máquina láser de precisión milimétrica para desintegrar el pegamento sin tocar tus componentes internos. Mano de obra quinientos pesos. ¡Escríbenos!",
        "copy_text": (
            "✨ ¿La tapa trasera de tu iPhone o Samsung parece telaraña? 🔨❌\n\n"
            "En las plazas usan pistolas de calor excesivo que queman las bobinas de carga inalámbrica MagSafe. En Volt Repair Studio usamos tecnología láser para desintegrar el epóxico de fábrica de forma milimétrica.\n\n"
            "💰 Mano de obra: Solo $500 MXN (+ tapa de cristal Grado A+)\n"
            "🛡️ Acabado original de fábrica y 90 días de garantía\n\n"
            "📲 Cotiza tu modelo por WhatsApp: +52 1 720 815 7790\n"
            "🌐 https://anubys6.github.io/volt-repair-studio/\n\n"
            "#TapaTrasera #iPhoneCristal #LaserRepair #VoltRepairStudio #TecnologiaMexico #iPhone14ProMax"
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
    """
    Crea un frame vertical 1080x1920 cinematográfico con estilo quirúrgico de laboratorio.
    """
    width, height = 1080, 1920
    
    # 1. Base oscura con textura
    base_img = Image.new("RGB", (width, height), color=(6, 9, 17))
    
    # Si existe imagen de fondo, cargarla y mezclarla con desenfoque
    bg_path = ASSETS_DIR / bg_image_name
    if bg_path.exists():
        try:
            bg = Image.open(str(bg_path)).convert("RGB")
            # Escalar manteniendo aspecto para cubrir 1080x1920
            ratio = max(width / bg.width, height / bg.height)
            new_w, new_h = int(bg.width * ratio), int(bg.height * ratio)
            bg = bg.resize((new_w, new_h), Image.Resampling.LANCZOS)
            crop_x = (new_w - width) // 2
            crop_y = (new_h - height) // 2
            bg = bg.crop((crop_x, crop_y, crop_x + width, crop_y + height))
            bg = bg.filter(ImageFilter.GaussianBlur(radius=18))
            # Oscurecer imagen al 25% para que el texto resalte de forma brutal
            darkener = Image.new("RGB", (width, height), (6, 9, 17))
            base_img = Image.blend(darkener, bg, alpha=0.28)
        except Exception:
            pass

    draw = ImageDraw.Draw(base_img)

    # Viñeta y halo de luz de color
    for y in range(0, 400):
        factor = (1 - (y / 400)) * 0.4
        draw.line([(0, y), (width, y)], fill=(int(accent_color[0] * factor), int(accent_color[1] * factor), int(accent_color[2] * factor)))

    # Fuentes
    font_badge = ImageFont.truetype(FONT_TITLE_PATH, 40)
    font_main = ImageFont.truetype(FONT_TITLE_PATH, 70)
    font_body = ImageFont.truetype(FONT_BODY_PATH, 46)
    font_cta = ImageFont.truetype(FONT_BODY_PATH, 42)
    font_brand = ImageFont.truetype(FONT_TITLE_PATH, 34)

    # 1. Encabezado de Marca (VOLT REPAIR STUDIO)
    draw.text((width // 2, 130), "⚡ VOLT REPAIR STUDIO ⚡", font=font_brand, fill=(148, 163, 184), anchor="mm")
    draw.line([(width // 2 - 180, 160), (width // 2 + 180, 160)], fill=(0, 240, 255), width=2)

    # 2. Badge Superior Destacado
    badge_bbox = draw.textbbox((0, 0), badge, font=font_badge)
    bw = badge_bbox[2] - badge_bbox[0] + 60
    bh = badge_bbox[3] - badge_bbox[1] + 28
    bx1 = (width - bw) // 2
    by1 = 230
    draw.rounded_rectangle([bx1, by1, bx1 + bw, by1 + bh], radius=24, fill=accent_color)
    draw.text((width // 2, by1 + bh // 2), badge, font=font_badge, fill=(255, 255, 255), anchor="mm")

    # 3. Título Principal (Gancho)
    title_lines = wrap_text(main_title, font_main, width - 140, draw)
    start_y = 440
    for line in title_lines:
        bbox = draw.textbbox((0, 0), line, font=font_main)
        lw = bbox[2] - bbox[0]
        lx = (width - lw) // 2
        # Sombra negra profunda
        draw.text((lx + 4, start_y + 4), line, font=font_main, fill=(0, 0, 0))
        text_color = secondary_color if stage == 1 else (255, 255, 255)
        draw.text((lx, start_y), line, font=font_main, fill=text_color)
        start_y += 88

    # 4. Separador Neón con Puntos
    draw.line([(180, start_y + 35), (width - 180, start_y + 35)], fill=accent_color, width=5)
    draw.ellipse([(width // 2 - 8, start_y + 29), (width // 2 + 8, start_y + 45)], fill=(255, 255, 255))
    start_y += 90

    # 5. Cuerpo Explicativo (Fórmula y Precio)
    body_lines = wrap_text(subtitle, font_body, width - 160, draw)
    for line in body_lines:
        bbox = draw.textbbox((0, 0), line, font=font_body)
        lw = bbox[2] - bbox[0]
        lx = (width - lw) // 2
        draw.text((lx + 3, start_y + 3), line, font=font_body, fill=(0, 0, 0))
        text_color = (255, 255, 255) if stage != 2 else secondary_color
        draw.text((lx, start_y), line, font=font_body, fill=text_color)
        start_y += 68

    # 6. Tarjeta Inferior de Llamada a la Acción (WhatsApp & Web)
    cta_box_y1 = 1500
    cta_box_y2 = 1690
    draw.rounded_rectangle([90, cta_box_y1, width - 90, cta_box_y2], radius=28, fill=(15, 23, 42), outline=accent_color, width=4)
    
    cta_lines = wrap_text(cta, font_cta, width - 220, draw)
    cy = cta_box_y1 + 45
    for line in cta_lines:
        draw.text((width // 2, cy), line, font=font_cta, fill=(255, 255, 255), anchor="mm")
        cy += 58

    # 7. Barra de Progreso Inferior según la etapa
    progress_y = height - 50
    draw.line([(60, progress_y), (width - 60, progress_y)], fill=(30, 41, 59), width=10)
    fill_ratio = stage / 3.0
    fill_w = int(60 + (width - 120) * fill_ratio)
    draw.line([(60, progress_y), (fill_w, progress_y)], fill=accent_color, width=10)

    base_img.save(str(output_path), quality=95)

async def synthesize_voice(text: str, output_path: Path):
    """Genera locución neural en español mexicano con ritmo enérgico y claro."""
    communicate = edge_tts.Communicate(
        text=text,
        voice="es-MX-JorgeNeural",
        rate="+5%",
        pitch="+0Hz"
    )
    await communicate.save(str(output_path))

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

    print(f"   [+] Generando locución neural con Edge-TTS...")
    asyncio.run(synthesize_voice(reel_data["narration"], audio_file))

    # Obtener duración exacta del audio con FFmpeg
    dur_cmd = [
        FFMPEG_EXE, "-i", str(audio_file),
        "-show_entries", "format=duration",
        "-v", "quiet", "-of", "csv=p=0"
    ]
    try:
        dur_res = subprocess.run(dur_cmd, capture_output=True, text=True)
        audio_dur = float(dur_res.stdout.strip())
    except Exception:
        audio_dur = 14.5

    print(f"   [+] Diseñando frames de alta resolución 1080x1920 (9:16)...")
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
        badge="📲 CONTACTO OFICIAL",
        main_title=reel_data["hook_text"],
        subtitle="Reparaciones activas garantizadas a domicilio.",
        cta=reel_data["cta_text"],
        accent_color=reel_data["accent_color"],
        secondary_color=(255, 230, 0),
        bg_image_name=reel_data["bg_image"],
        output_path=card3_file,
        stage=3
    )

    # Duraciones calibradas
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

    print(f"   [+] Codificando video final MP4 con FFmpeg ({audio_dur:.1f}s)...")
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

    # Guardar archivo de texto de copia
    copy_file = EXPORT_DIR / f"{reel_id}_texto_redes.txt"
    with open(copy_file, "w", encoding="utf-8") as f:
        f.write("=== TEXTO LISTO PARA PEGAR EN TIKTOK, INSTAGRAM O FACEBOOK REELS ===\n\n")
        f.write(reel_data["copy_text"])

    print(f"   [✓] Video generado: {final_video.name}")
    print(f"   [✓] Copia con hashtags guardada: {copy_file.name}")

    return {
        "video": final_video,
        "copy": copy_file,
        "duration": audio_dur
    }

def main():
    print("=" * 80)
    print(" ⚡ VOLT REPAIR STUDIO — GENERADOR AUTOMATIZADO DE REELS & TIKTOKS (9:16)")
    print("   Arquitectura Anti-Slop con Locución Neural y Render Quirúrgico")
    print("=" * 80)
    
    generated = []
    for idx, reel in enumerate(REELS_DATA, start=1):
        print(f"\n🎬 Generando Video [{idx}/{len(REELS_DATA)}]: {reel['tema']} -> '{reel['hook_text']}'")
        try:
            res = build_reel_video(reel)
            generated.append(res)
        except Exception as e:
            print(f"   ❌ Error generando reel {reel['id']}: {e}")

    print("\n" + "=" * 80)
    print(f" ✨ ¡PROCESO FINALIZADO CON ÉXITO! Se generaron {len(generated)} videos en:")
    print(f" 📁 {EXPORT_DIR}")
    print("=" * 80)

if __name__ == "__main__":
    main()
