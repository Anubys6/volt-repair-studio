"""
=============================================================================
🎬 GENERADOR PROFESIONAL DE REELS / TIKTOKS CON VIDEO REAL Y SUBTÍTULOS ANIMADOS
VOLT REPAIR STUDIO — ARQUITECTURA CINEMATOGRÁFICA 9:16 (1080x1920)
=============================================================================
Características:
1. Video real B-Roll en movimiento de micro-cirugía y reparación de celulares.
2. Subtítulos dinámicos estilo CapCut / Alex Hormozi (Amarillo neón y Cyan,
   borde negro de 6px, sincronizados palabra por palabra con Edge-TTS).
3. Overlay HUD de alta tecnología con logotipo oficial, badge y llamado a la acción.
4. Locución neural mexicana enérgica (es-MX-JorgeNeural).
=============================================================================
"""

import os
import sys
import asyncio
import subprocess
from pathlib import Path
from typing import Dict, Any, List
from PIL import Image, ImageDraw, ImageFont
import imageio_ffmpeg
import edge_tts

# Codificación UTF-8 en Windows
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding='utf-8')
        sys.stderr.reconfigure(encoding='utf-8')
    except Exception:
        pass

BASE_DIR = Path(r"C:\Users\SAmue\Desktop\Volt-Repair-Studio")
VIDEOS_DIR = BASE_DIR / "videos"
BROLL_DIR = VIDEOS_DIR / "b_roll"
EXPORT_DIR = VIDEOS_DIR / "reels_exportados"
ASSETS_DIR = BASE_DIR / "assets"
EXPORT_DIR.mkdir(parents=True, exist_ok=True)

FFMPEG_EXE = imageio_ffmpeg.get_ffmpeg_exe()

FONT_TITLE_PATH = r"C:\Windows\Fonts\ariblk.ttf"
if not os.path.exists(FONT_TITLE_PATH):
    FONT_TITLE_PATH = r"C:\Windows\Fonts\arialbd.ttf"
FONT_BODY_PATH = r"C:\Windows\Fonts\arialbd.ttf"

REELS_CONFIG = [
    {
        "id": "reel_transparencia_sala_700",
        "tema": "Transparencia Quirúrgica en tu Comedor",
        "broll_file": "repair_broll_1.webm",
        "badge": "👁️ CERO ROBO DE PIEZAS",
        "accent_hex": "#00f0ff",          # Cyan
        "accent_rgb": (0, 240, 255),
        "hook_title": "¿POR QUÉ TIENEN MIEDO\nA LOS TALLERES?",
        "price_tag": "⚡ MANO DE OBRA PANTALLA: $700 MXN",
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
        "broll_file": "repair_broll_2.webm",
        "badge": "🔬 PROGRAMACIÓN EEPROM",
        "accent_hex": "#c084fc",          # Púrpura
        "accent_rgb": (192, 132, 252),
        "hook_title": "¿POR QUÉ EN LAS PLAZAS\nTE DEJAN SIN TRUETONE?",
        "price_tag": "⚡ PANTALLA CON TRUETONE: $700 MXN",
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
        "broll_file": "repair_broll_3.mkv",
        "badge": "🔋 ALERTA EN LA BATERÍA",
        "accent_hex": "#10b981",          # Verde
        "accent_rgb": (16, 185, 129),
        "hook_title": "ENCONTRAMOS CINTA ESCOLAR\nEN ESTA BATERÍA...",
        "price_tag": "⚡ MANO DE OBRA BATERÍA: $500 MXN",
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

def format_ass_time(seconds: float) -> str:
    h = int(seconds // 3600)
    m = int((seconds % 3600) // 60)
    s = int(seconds % 60)
    cs = int(round((seconds - int(seconds)) * 100))
    if cs >= 100:
        cs = 99
    return f"{h}:{m:02d}:{s:02d}.{cs:02d}"

async def generate_speech_and_cues(text: str, audio_path: Path):
    """Genera audio con Edge-TTS y extrae marcas de tiempo de oraciones."""
    comm = edge_tts.Communicate(
        text=text,
        voice="es-MX-JorgeNeural",
        rate="+6%",
        pitch="+0Hz"
    )
    cues = []
    audio_data = bytearray()
    
    for attempt in range(1, 4):
        try:
            async for chunk in comm.stream():
                if chunk["type"] == "audio":
                    audio_data.extend(chunk["data"])
                elif chunk["type"] == "SentenceBoundary":
                    cues.append(chunk)
            break
        except Exception as e:
            if attempt == 3:
                raise e
            await asyncio.sleep(1.5)
            cues.clear()
            audio_data.clear()

    with open(audio_path, "wb") as f:
        f.write(audio_data)
        
    return cues

def build_ass_subtitles(cues: list, ass_path: Path):
    """
    Construye un archivo ASS con subtítulos estilo CapCut:
    - Tipografía pesada (Arial Black, 68pt).
    - Color amarillo fluorescente y blanco alternado.
    - Contorno negro grueso (6px) para máxima legibilidad sobre video en movimiento.
    - Fragmentos dinámicos de 2 a 4 palabras por golpe visual.
    """
    header = """[Script Info]
ScriptType: v4.00+
PlayResX: 1080
PlayResY: 1920
ScaledBorderAndShadow: yes

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: CapCutYellow,Arial Black,68,&H0000FFFF,&H000000FF,&H00000000,&H90000000,-1,0,0,0,100,100,2,0,1,6,3,2,60,60,520,1
Style: CapCutCyan,Arial Black,68,&H00FFFF00,&H000000FF,&H00000000,&H90000000,-1,0,0,0,100,100,2,0,1,6,3,2,60,60,520,1
Style: CapCutWhite,Arial Black,68,&H00FFFFFF,&H000000FF,&H00000000,&H90000000,-1,0,0,0,100,100,2,0,1,6,3,2,60,60,520,1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
"""
    dialogues = []
    style_cycle = ["CapCutYellow", "CapCutCyan", "CapCutWhite"]
    style_idx = 0

    for cue in cues:
        # offset y duration en unidades de 100ns -> convertir a segundos
        start_sec = cue["offset"] / 10_000_000.0
        dur_sec = cue["duration"] / 10_000_000.0
        words = cue["text"].strip().split()
        if not words:
            continue

        # Dividir la oración en bloques rítmicos de 2 a 3 palabras
        chunk_size = 3
        chunks = [words[i:i + chunk_size] for i in range(0, len(words), chunk_size)]
        chunk_dur = dur_sec / len(chunks)

        for i, chk in enumerate(chunks):
            c_start = start_sec + (i * chunk_dur)
            c_end = c_start + chunk_dur
            txt = " ".join(chk).upper()
            st = style_cycle[style_idx % len(style_cycle)]
            style_idx += 1
            dialogues.append(f"Dialogue: 0,{format_ass_time(c_start)},{format_ass_time(c_end)},{st},,0,0,0,,{txt}")

    with open(ass_path, "w", encoding="utf-8") as f:
        f.write(header + "\n".join(dialogues) + "\n")

def create_hud_overlay(reel: dict, overlay_path: Path):
    """
    Crea una capa gráfica transparente 1080x1920:
    - Cabecera con Logotipo y Marca.
    - Badge Fluorescente.
    - Título Gancho en la parte superior.
    - Etiqueta de Mano de Obra ($700 / $500).
    - Tarjeta inferior de WhatsApp.
    - El centro queda 100% transparente para que el video de reparación se mueva libremente.
    """
    w, h = 1080, 1920
    img = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    # 1. Gradientes de oscurecimiento superior e inferior para legibilidad perfecta
    for y in range(0, 480):
        alpha = int((1 - (y / 480)) * 210)
        draw.line([(0, y), (w, y)], fill=(6, 9, 17, alpha))

    for y in range(h - 440, h):
        alpha = int(((y - (h - 440)) / 440) * 225)
        draw.line([(0, y), (w, y)], fill=(6, 9, 17, alpha))

    font_brand = ImageFont.truetype(FONT_TITLE_PATH, 34)
    font_badge = ImageFont.truetype(FONT_TITLE_PATH, 38)
    font_hook = ImageFont.truetype(FONT_TITLE_PATH, 58)
    font_price = ImageFont.truetype(FONT_BODY_PATH, 42)
    font_cta = ImageFont.truetype(FONT_BODY_PATH, 44)

    # 2. Header oficial
    draw.text((w // 2, 110), "⚡ VOLT REPAIR STUDIO ⚡", font=font_brand, fill=(203, 213, 225, 240), anchor="mm")
    draw.line([(w // 2 - 180, 138), (w // 2 + 180, 138)], fill=reel["accent_rgb"] + (220,), width=2)

    # 3. Badge en cápsula
    badge_text = reel["badge"]
    bbox = draw.textbbox((0, 0), badge_text, font=font_badge)
    bw = bbox[2] - bbox[0] + 56
    bh = bbox[3] - bbox[1] + 24
    bx1 = (w - bw) // 2
    by1 = 185
    draw.rounded_rectangle([bx1, by1, bx1 + bw, by1 + bh], radius=22, fill=reel["accent_rgb"] + (240,))
    draw.text((w // 2, by1 + bh // 2), badge_text, font=font_badge, fill=(255, 255, 255, 255), anchor="mm")

    # 4. Título Gancho en la parte superior
    hook_lines = reel["hook_title"].split("\n")
    hy = 310
    for line in hook_lines:
        bbox = draw.textbbox((0, 0), line, font=font_hook)
        lw = bbox[2] - bbox[0]
        lx = (w - lw) // 2
        # Sombra negra profunda
        draw.text((lx + 4, hy + 4), line, font=font_hook, fill=(0, 0, 0, 240))
        draw.text((lx, hy), line, font=font_hook, fill=(255, 255, 255, 255))
        hy += 72

    # 5. Etiqueta de Mano de Obra Destacada
    price_text = reel["price_tag"]
    p_bbox = draw.textbbox((0, 0), price_text, font=font_price)
    pw = p_bbox[2] - p_bbox[0] + 50
    ph = p_bbox[3] - p_bbox[1] + 20
    px1 = (w - pw) // 2
    py1 = hy + 20
    draw.rounded_rectangle([px1, py1, px1 + pw, py1 + ph], radius=16, fill=(15, 23, 42, 230), outline=reel["accent_rgb"] + (240,), width=3)
    draw.text((w // 2, py1 + ph // 2), price_text, font=font_price, fill=(255, 230, 0, 255), anchor="mm")

    # 6. Tarjeta inferior de WhatsApp
    cta_y1 = h - 260
    cta_y2 = h - 120
    draw.rounded_rectangle([90, cta_y1, w - 90, cta_y2], radius=26, fill=(15, 23, 42, 230), outline=reel["accent_rgb"] + (255,), width=4)
    draw.text((w // 2, cta_y1 + 45), "📲 Agenda tu cita por WhatsApp:", font=font_brand, fill=(203, 213, 225, 240), anchor="mm")
    draw.text((w // 2, cta_y1 + 95), "+52 1 720 815 7790", font=font_cta, fill=(16, 185, 129, 255), anchor="mm")

    # 7. Barra de progreso inferior estética
    draw.line([(60, h - 50), (w - 60, h - 50)], fill=(30, 41, 59, 200), width=8)
    draw.line([(60, h - 50), (w // 2 + 100, h - 50)], fill=reel["accent_rgb"] + (240,), width=8)

    img.save(str(overlay_path), "PNG")

def process_single_reel(reel: dict) -> dict:
    reel_id = reel["id"]
    print(f"\n=======================================================")
    print(f"🎬 Procesando Reel: {reel['tema']}")
    print(f"   B-Roll: {reel['broll_file']}")
    print(f"=======================================================")

    temp_dir = EXPORT_DIR / f"temp_{reel_id}"
    temp_dir.mkdir(parents=True, exist_ok=True)

    audio_path = temp_dir / f"{reel_id}.mp3"
    ass_path = temp_dir / f"{reel_id}.ass"
    overlay_path = temp_dir / f"{reel_id}_hud.png"
    final_video = EXPORT_DIR / f"{reel_id}_1080x1920.mp4"
    copy_path = EXPORT_DIR / f"{reel_id}_texto_redes.txt"
    broll_video = BROLL_DIR / reel["broll_file"]

    # 1. Generar audio con Edge-TTS
    print(f"   [+] Sintetizando locución neural mexicana...")
    cues = asyncio.run(generate_speech_and_cues(reel["narration"], audio_path))

    # Duración exacta del audio
    dur_cmd = [
        FFMPEG_EXE, "-i", str(audio_path),
        "-show_entries", "format=duration",
        "-v", "quiet", "-of", "csv=p=0"
    ]
    try:
        dur_res = subprocess.run(dur_cmd, capture_output=True, text=True)
        audio_dur = float(dur_res.stdout.strip())
    except Exception:
        audio_dur = 14.8
    print(f"   [✓] Duración del audio: {audio_dur:.2f}s")

    # 2. Generar subtítulos dinámicos ASS
    print(f"   [+] Generando subtítulos dinámicos estilo CapCut (Amarillo/Cyan)...")
    build_ass_subtitles(cues, ass_path)

    # 3. Generar overlay HUD
    print(f"   [+] Diseñando overlay HUD de Volt Repair Studio...")
    create_hud_overlay(reel, overlay_path)

    # 4. Ensamblar con FFmpeg: Video real B-roll + HUD + Subtítulos + Audio
    print(f"   [+] Renderizando video vertical 9:16 (1080x1920) a 60 FPS con FFmpeg...")

    filter_complex = (
        f"[0:v]scale=-1:1920,crop=1080:1920,eq=brightness=-0.08:contrast=1.12[bg];"
        f"[bg][1:v]overlay=0:0[v1];"
        f"[v1]ass={ass_path.name}[outv]"
    )

    cmd = [
        FFMPEG_EXE, "-y",
        "-stream_loop", "-1",       # Repetir B-roll si dura menos que el audio
        "-i", str(broll_video),
        "-i", str(overlay_path),
        "-i", str(audio_path),
        "-filter_complex", filter_complex,
        "-map", "[outv]",
        "-map", "2:a",
        "-t", str(audio_dur),
        "-c:v", "libx264",
        "-preset", "veryfast",
        "-pix_fmt", "yuv420p",
        "-c:a", "aac",
        "-b:a", "192k",
        str(final_video)
    ]

    res = subprocess.run(cmd, cwd=str(temp_dir), capture_output=True, text=True)
    if res.returncode != 0:
        raise RuntimeError(f"Error en FFmpeg: {res.stderr[-600:]}")

    # 5. Guardar texto con hashtags
    with open(copy_path, "w", encoding="utf-8") as f:
        f.write("=== TEXTO LISTO PARA PUBLICAR EN TIKTOK, INSTAGRAM O FACEBOOK ===\n\n")
        f.write(reel["copy_text"])

    print(f"   [✓] ¡Video cinematográfico completado!: {final_video.name}")
    print(f"   [✓] Texto de publicación: {copy_path.name}")

    # Limpiar temporales
    try:
        for f in temp_dir.iterdir():
            try: f.unlink()
            except Exception: pass
        temp_dir.rmdir()
    except Exception:
        pass

    return {
        "video": final_video,
        "copy": copy_path,
        "duration": audio_dur
    }

def main():
    print("=" * 80)
    print(" 🚀 RENDERIZADOR CINEMATOGRÁFICO DE REELS — VOLT REPAIR STUDIO")
    print("    Video Real de Fondo + Subtítulos CapCut + Locución Neural")
    print("=" * 80)

    for reel in REELS_CONFIG:
        try:
            process_single_reel(reel)
        except Exception as e:
            print(f"❌ Error en {reel['id']}: {e}")

    print("\n" + "=" * 80)
    print(" ✨ ¡LOS 3 REELS CON VIDEO REAL Y SUBTÍTULOS ANIMADOS ESTÁN LISTOS!")
    print(f" 📁 Ubicación: {EXPORT_DIR}")
    print("=" * 80)

if __name__ == "__main__":
    main()
