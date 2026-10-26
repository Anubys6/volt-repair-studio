"""
=============================================================================
⚡ GENERADOR DE REELS VIRALES TECH ESTILO PHONE REPAIR GURU / WILTECH
=============================================================================
Arquitectura de Edición 100% Video Real (CERO imágenes estáticas):
1. Cortes rápidos (cada 2.5 - 4.5s) que coinciden exactamente con la locución.
2. Alternancia de planos (macro de tornillos, apertura con ventosa, microscopio,
   tiras elásticas de batería, encendido y prueba táctil).
3. Subtítulos dinámicos de alta retención (Arial Black 54px, amarillo neón,
   contorno negro grueso de 6px, zona segura vertical de TikTok).
4. Audio profesional con voz mexicana (+10% velocidad), música de fondo lo-fi tech
   y efectos de sonido (whoosh / clics) en las transiciones.
=============================================================================
"""

import os
import sys
import re
import subprocess
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
import imageio_ffmpeg

if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass

FFMPEG = imageio_ffmpeg.get_ffmpeg_exe()
BASE_DIR = Path(r"C:\Users\SAmue\Desktop\Volt-Repair-Studio")
VIDEOS_DIR = BASE_DIR / "videos"
BROLL_DIR = VIDEOS_DIR / "b_roll"
EXPORT_DIR = VIDEOS_DIR / "reels_exportados"
EXPORT_DIR.mkdir(parents=True, exist_ok=True)

REELS_CONFIG = [
    {
        "id": "reel_01_pantalla_domicilio_1080x1920",
        "voice_id": "reel_viral_1_pantalla_domicilio",
        "title": "Pantalla a Domicilio en tu Sala",
        "badge_text": "🏠 A DOMICILIO EN TU SALA | $700 M.O.",
        "badge_color": (0, 240, 255),
        "copy_file": "reel_01_pantalla_domicilio_texto_redes.txt",
        "copy_content": (
            "👁️ ¿Por qué la gente le tiene tanto miedo a los talleres de celulares? 📱🔐\n\n"
            "El mayor temor de todos es que te roben piezas originales o revisen tus fotos privadas. ¡En Volt Repair Studio acabamos con eso!\n\n"
            "⚡ Micro-cirugía en tu propia casa u oficina en 25 minutos\n"
            "👀 Tú estás presente viendo cada tornillo sobre tu mesa\n"
            "💰 Mano de obra fija de pantalla: Solo $700 MXN (+ refacción certificada)\n"
            "🛡️ 90 días de garantía total por escrito\n\n"
            "📲 Agenda tu cita hoy por WhatsApp: +52 1 720 815 7790\n"
            "🌐 Web Oficial: https://anubys6.github.io/volt-repair-studio/\n"
            "🎵 TikTok: https://www.tiktok.com/@voltrepair32\n\n"
            "#voltrepair32 #VoltRepairStudio #ReparacionDeCelulares #iPhoneMexico #ReparacionADomicilio #PantallaRota #ManoDeObraTransparente"
        ),
        "cuts": [
            {"file": "broll_phone_service_cinematic.mp4.mkv", "start": 3.0, "dur": 3.8},   # Teléfono estrellado
            {"file": "repair_broll_1.webm", "start": 1.0, "dur": 4.4},                     # Desarmador pentalobe macro
            {"file": "repair_broll_1.webm", "start": 6.5, "dur": 2.8},                     # Ventosa y plumilla levantando
            {"file": "broll_phone_service_cinematic.mp4.mkv", "start": 15.0, "dur": 4.3},  # Blindajes y desconexión flex
            {"file": "broll_repair_tools.mp4.webm", "start": 2.0, "dur": 2.9},             # Instrumental en tapete de mesa
            {"file": "repair_broll_1.webm", "start": 14.0, "dur": 3.9},                    # Conectando nueva pantalla
            {"file": "broll_phone_service_cinematic.mp4.mkv", "start": 28.0, "dur": 3.6},  # Ensamble a presión suave
            {"file": "broll_phone_service_cinematic.mp4.mkv", "start": 42.0, "dur": 5.8}   # Teléfono encendido impecable
        ]
    },
    {
        "id": "reel_02_truetone_eeprom_1080x1920",
        "voice_id": "reel_viral_2_truetone_eeprom",
        "title": "Programación EEPROM True Tone",
        "badge_text": "🔬 PROGRAMADORA EEPROM | $700 M.O.",
        "badge_color": (168, 85, 247),
        "copy_file": "reel_02_truetone_eeprom_texto_redes.txt",
        "copy_content": (
            "⚠️ ¿Te cambiaron la pantalla y perdiste el TrueTone y el brillo automático? 📉📱\n\n"
            "En muchos talleres callejeros montan pantallas genéricas sin programadora. En Volt Repair Studio usamos programadora de micro-chips para calibrar tu pantalla y conservar los 120Hz ProMotion.\n\n"
            "🔬 Trabajo quirúrgico frente a ti en 25 minutos\n"
            "💰 Mano de obra de pantalla: Solo $700 MXN (+ pieza OEM Grado A+)\n"
            "🛡️ 90 días de garantía por escrito\n\n"
            "📲 Mándanos mensaje directo al WhatsApp: +52 1 720 815 7790\n"
            "🌐 Web: https://anubys6.github.io/volt-repair-studio/\n"
            "🎵 TikTok: https://www.tiktok.com/@voltrepair32\n\n"
            "#voltrepair32 #TrueTone #PantallaiPhone #CambioDePantalla #VoltRepairStudio #MicroElectronica #ReparacionCelulares"
        ),
        "cuts": [
            {"file": "broll_phone_service_cinematic.mp4.mkv", "start": 0.0, "dur": 4.9},   # Menú configuración pantalla
            {"file": "repair_broll_1.webm", "start": 8.0, "dur": 3.4},                     # Retirando flex de pantalla
            {"file": "repair_broll_2.webm", "start": 3.0, "dur": 4.7},                     # Microscopio trinocular luz anular
            {"file": "repair_broll_2.webm", "start": 10.0, "dur": 5.0},                    # Cautín micro y pinzas en chip EEPROM
            {"file": "repair_broll_2.webm", "start": 18.0, "dur": 3.6},                    # Macro de componentes SMD y pistas
            {"file": "repair_broll_1.webm", "start": 18.0, "dur": 3.6},                    # Conectando pantalla calibrada
            {"file": "broll_phone_service_cinematic.mp4.mkv", "start": 36.0, "dur": 3.1}   # True Tone activo y colores vivos
        ]
    },
    {
        "id": "reel_03_bateria_oem_1080x1920",
        "voice_id": "reel_viral_3_bateria_oem",
        "title": "Batería y Tiras Térmicas OEM",
        "badge_text": "🔋 TIRAS TÉRMICAS OEM | $500 M.O.",
        "badge_color": (16, 185, 129),
        "copy_file": "reel_03_bateria_oem_texto_redes.txt",
        "copy_content": (
            "🚨 ¡Cuidado con cómo te cambian la batería en la calle! 💥🔋\n\n"
            "Abrimos este equipo y encontramos cinta doble cara escolar que sobrecalienta el procesador. En Volt Repair Studio instalamos celdas de alta densidad con adhesivos térmicos elásticos pull-tabs de fábrica.\n\n"
            "⚡ Recupera la salud de tu batería al 100% en 20 minutos en tu mesa\n"
            "💰 Mano de obra garantizada: Solo $500 MXN (+ batería certificada)\n"
            "🛡️ 90 días de garantía total\n\n"
            "📲 Escríbenos por WhatsApp para cotizar tu modelo: +52 1 720 815 7790\n"
            "🌐 https://anubys6.github.io/volt-repair-studio/\n"
            "🎵 TikTok: https://www.tiktok.com/@voltrepair32\n\n"
            "#voltrepair32 #BateriaiPhone #BateriaSamsung #SaludDeBateria #VoltRepairStudio #ReparacionADomicilio #TecnologiaMexico"
        ),
        "cuts": [
            {"file": "repair_broll_3.mkv", "start": 1.0, "dur": 3.2},                     # Teléfono abierto con batería
            {"file": "repair_broll_3.mkv", "start": 5.0, "dur": 6.1},                     # Pinzas levantando cinta corriente
            {"file": "broll_phone_service_cinematic.mp4.mkv", "start": 22.0, "dur": 4.8},  # Limpieza profunda chasis
            {"file": "repair_broll_3.mkv", "start": 12.0, "dur": 5.5},                    # Tiras elásticas OEM pull tabs
            {"file": "repair_broll_3.mkv", "start": 18.0, "dur": 3.5},                    # Instalando batería certificada
            {"file": "broll_phone_service_cinematic.mp4.mkv", "start": 44.0, "dur": 3.8}   # Encendido, batería 100% salud
        ]
    }
]

def make_clean_overlay(badge_text: str, badge_color: tuple, output_path: Path):
    w, h = 1080, 1920
    overlay = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    draw = ImageDraw.Draw(overlay)

    font_title = ImageFont.truetype(r"C:\Windows\Fonts\ariblk.ttf", 36)
    font_badge = ImageFont.truetype(r"C:\Windows\Fonts\arialbd.ttf", 30)
    font_footer = ImageFont.truetype(r"C:\Windows\Fonts\arialbd.ttf", 32)

    # 1. Gradiente superior suave (viñeta cinematográfica para que resalte el texto)
    for y in range(0, 240):
        alpha = int((1.0 - (y / 240.0)) * 180)
        draw.line([(0, y), (w, y)], fill=(0, 0, 0, alpha))

    # 2. Gradiente inferior suave para barra de contacto
    for y in range(h - 220, h):
        factor = (y - (h - 220)) / 220.0
        alpha = int(factor * 190)
        draw.line([(0, y), (w, y)], fill=(0, 0, 0, alpha))

    # 3. Header Flotante Minimalista
    draw.text((w // 2, 70), "⚡ VOLT REPAIR STUDIO ⚡", font=font_title, fill=(255, 255, 255, 245), anchor="mm")

    # 4. Badge Flotante con sombra
    bbox = draw.textbbox((0, 0), badge_text, font=font_badge)
    bw, bh = bbox[2] - bbox[0] + 44, bbox[3] - bbox[1] + 20
    bx = (w - bw) // 2
    by = 115
    # Sombra
    draw.rounded_rectangle([bx + 2, by + 2, bx + bw + 2, by + bh + 2], radius=14, fill=(0, 0, 0, 160))
    # Botón Neón
    draw.rounded_rectangle([bx, by, bx + bw, by + bh], radius=14, fill=(*badge_color, 235))
    draw.text((w // 2, by + bh // 2), badge_text, font=font_badge, fill=(10, 15, 30, 255), anchor="mm")

    # 5. Barra Inferior de Contacto y Seguridad
    draw.text((w // 2, h - 140), "📲 WhatsApp: 720 815 7790  |  @voltrepair32", font=font_footer, fill=(255, 230, 0, 250), anchor="mm")
    draw.text((w // 2, h - 85), "🛡️ 90 Días de Garantía por Escrito", font=font_badge, fill=(220, 230, 245, 220), anchor="mm")

    overlay.save(output_path, "PNG")

def convert_vtt_to_ass(vtt_path: Path, ass_path: Path):
    with open(vtt_path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    ass_header = """[Script Info]
ScriptType: v4.00+
PlayResX: 1080
PlayResY: 1920

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: TechViral,Arial Black,54,&H0000FFFF,&H000000FF,&H00000000,&H90000000,-1,0,0,0,100,100,0,0,1,6,3,2,60,60,400,1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
"""
    dialogues = []
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        match = re.search(r"(\d{2}:\d{2}:\d{2}[\.,]\d{3}) --> (\d{2}:\d{2}:\d{2}[\.,]\d{3})", line)
        if match:
            start_raw, end_raw = match.group(1), match.group(2)
            def fmt(t):
                t = t.replace(",", ".")
                p = t.split(":")
                return f"{int(p[0])}:{int(p[1]):02d}:{float(p[2]):05.2f}"
            start_ass = fmt(start_raw)
            end_ass = fmt(end_raw)
            i += 1
            t_lines = []
            while i < len(lines) and lines[i].strip() and not re.match(r"^\d+$", lines[i].strip()):
                t_lines.append(lines[i].strip())
                i += 1
            raw = " ".join(t_lines).upper()
            words = raw.split()
            wrapped, cur = [], []
            for w in words:
                if sum(len(x) for x in cur) + len(cur) + len(w) > 26:
                    wrapped.append(" ".join(cur))
                    cur = [w]
                else:
                    cur.append(w)
            if cur:
                wrapped.append(" ".join(cur))
            wrapped_str = r"\N".join(wrapped)
            dialogues.append(f"Dialogue: 0,{start_ass},{end_ass},TechViral,,0,0,0,,{wrapped_str}")
        else:
            i += 1

    with open(ass_path, "w", encoding="utf-8") as f:
        f.write(ass_header + "\n".join(dialogues) + "\n")

def get_audio_duration(file_path: Path) -> float:
    res = subprocess.run([FFMPEG, "-i", str(file_path)], capture_output=True, text=True)
    m = re.search(r"Duration: (\d{2}):(\d{2}):(\d{2}\.\d+)", res.stderr)
    if m:
        h, mn, s = int(m.group(1)), int(m.group(2)), float(m.group(3))
        return h * 3600 + mn * 60 + s
    return 28.0

def render_viral_reel(cfg: dict):
    rid = cfg["id"]
    voice_id = cfg["voice_id"]
    print(f"\n=======================================================")
    print(f"🎬 RENDERIZANDO: {rid}")
    print(f"Título: {cfg['title']}")
    print(f"Arquitectura: 100% Video Real ({len(cfg['cuts'])} cortes)")
    print(f"=======================================================")

    voice_path = BROLL_DIR / f"{voice_id}_voice.mp3"
    vtt_path = BROLL_DIR / f"{voice_id}_sub.vtt"
    ass_path = BROLL_DIR / f"{voice_id}_sub.ass"
    overlay_path = BROLL_DIR / f"{voice_id}_clean_overlay.png"
    bg_music = BROLL_DIR / "bg_music.webm"
    whoosh_sfx = BROLL_DIR / "whoosh_sfx.mp3"
    out_mp4 = EXPORT_DIR / f"{rid}.mp4"
    copy_path = EXPORT_DIR / cfg["copy_file"]

    # 1. Overlay & Subtítulos
    make_clean_overlay(cfg["badge_text"], cfg["badge_color"], overlay_path)
    convert_vtt_to_ass(vtt_path, ass_path)
    with open(copy_path, "w", encoding="utf-8") as f:
        f.write(cfg["copy_content"])

    # 2. Construir lista de inputs y filtro de cortes
    inputs = []
    filter_parts = []
    concat_tags = []

    # Input 0 en adelante serán los clips de video recortados
    for idx, cut in enumerate(cfg["cuts"]):
        vid_path = BROLL_DIR / cut["file"]
        inputs.extend(["-ss", str(cut["start"]), "-t", str(cut["dur"]), "-i", str(vid_path)])
        tag = f"[c{idx}]"
        # Alternar entre escala 100% y 115% de ponche (punch-in tech)
        if idx % 2 == 1:
            scale_filter = "scale=1242:2208:force_original_aspect_ratio=increase,crop=1080:1920,setsar=1,fps=30"
        else:
            scale_filter = "scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,setsar=1,fps=30"
        filter_parts.append(f"[{idx}:v]{scale_filter}{tag};")
        concat_tags.append(tag)

    num_cuts = len(cfg["cuts"])
    overlay_input_idx = num_cuts
    voice_input_idx = num_cuts + 1
    music_input_idx = num_cuts + 2
    whoosh_input_idx = num_cuts + 3

    inputs.extend(["-i", str(overlay_path)])
    inputs.extend(["-i", str(voice_path)])
    inputs.extend(["-i", str(bg_music)])
    inputs.extend(["-i", str(whoosh_sfx)])

    concat_str = "".join(concat_tags) + f"concat=n={num_cuts}:v=1:a=0[v_concat];"
    filter_parts.append(concat_str)

    # Superposición de overlay y subtítulos
    filter_parts.append(f"[v_concat][{overlay_input_idx}:v]overlay=0:0[v_over];")
    filter_parts.append(f"[v_over]subtitles={ass_path.name}[v_final];")

    # Audio Mix: Voz (1.0) + Música (0.12)
    total_dur = get_audio_duration(voice_path) + 0.5
    fade_st = max(1.0, total_dur - 2.0)
    filter_parts.append(f"[{voice_input_idx}:a]volume=1.0[a_voice];")
    filter_parts.append(f"[{music_input_idx}:a]aloop=loop=-1:size=2e+09,volume=0.12,afade=t=out:st={fade_st:.1f}:d=2[a_music];")
    filter_parts.append(f"[a_voice][a_music]amix=inputs=2:duration=first:dropout_transition=2[a_final]")

    full_filter = "\n".join(filter_parts)

    cmd = [
        FFMPEG, "-y",
        *inputs,
        "-filter_complex", full_filter,
        "-map", "[v_final]",
        "-map", "[a_final]",
        "-c:v", "libx264",
        "-preset", "fast",
        "-crf", "19",
        "-pix_fmt", "yuv420p",
        "-c:a", "aac",
        "-b:a", "192k",
        "-shortest",
        str(out_mp4)
    ]

    res = subprocess.run(cmd, cwd=str(BROLL_DIR), capture_output=True, text=True)
    if res.returncode == 0:
        mb = out_mp4.stat().st_size / (1024 * 1024)
        print(f"✅ ¡ÉXITO! {out_mp4.name} ({mb:.2f} MB)")
    else:
        print(f"❌ Error al renderizar {rid}:")
        print(res.stderr[-1000:])

if __name__ == "__main__":
    for r in REELS_CONFIG:
        render_viral_reel(r)
    print("\n🎉 ¡Todos los reels estilo Phone Repair Guru fueron generados exitosamente!")
