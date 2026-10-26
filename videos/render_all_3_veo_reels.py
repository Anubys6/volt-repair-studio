"""
=============================================================================
⚡ GENERADOR DE 3 REELS VERTICALES DE ALTA PRODUCCIÓN — VOLT REPAIR STUDIO
=============================================================================
Basado en la metodología aprendida de Google Veo / Gemini (Eldrin Lobo):
- Visuales Ultra-Realistas 9:16 de Personaje Técnico
- Cortes dinámicos con B-roll 4K de microcirugía y herramientas
- Subtítulos cinemáticos en zona segura (amarillo/blanco con sombra y contorno)
- Locución mexicana fluida (es-MX-JorgeNeural) + música tech lo-fi
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
        "voice_id": "reel_1_pantalla_domicilio",
        "badge_text": "🏠 A DOMICILIO EN TU SALA | $700 MANO DE OBRA",
        "badge_color": (0, 240, 255),
        "hero_image": "volt_tech_living_room.jpg",
        "broll_video": "repair_broll_1.webm",
        "broll_start": 2.0,
        "broll_duration": 12.0,
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
        )
    },
    {
        "id": "reel_02_truetone_eeprom_1080x1920",
        "voice_id": "reel_2_truetone_eeprom",
        "badge_text": "🔬 PROGRAMADORA EEPROM | $700 MANO DE OBRA",
        "badge_color": (168, 85, 247),
        "hero_image": "volt_tech_lab_truetone.jpg",
        "broll_video": "repair_broll_2.webm",
        "broll_start": 3.0,
        "broll_duration": 11.5,
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
        )
    },
    {
        "id": "reel_03_bateria_oem_1080x1920",
        "voice_id": "reel_3_bateria_oem",
        "badge_text": "🔋 TIRAS TÉRMICAS OEM | $500 MANO DE OBRA",
        "badge_color": (16, 185, 129),
        "hero_image": "volt_tech_battery_pulltabs.jpg",
        "broll_video": "repair_broll_3.mkv",
        "broll_start": 2.0,
        "broll_duration": 11.5,
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
        )
    }
]

def make_overlay(badge_text: str, badge_color: tuple, output_path: Path):
    w, h = 1080, 1920
    overlay = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    draw = ImageDraw.Draw(overlay)

    font_title = ImageFont.truetype(r"C:\Windows\Fonts\ariblk.ttf", 38)
    font_badge = ImageFont.truetype(r"C:\Windows\Fonts\arialbd.ttf", 32)
    font_footer = ImageFont.truetype(r"C:\Windows\Fonts\arialbd.ttf", 34)

    # Top Header Background
    draw.rectangle([0, 0, w, 220], fill=(10, 15, 30, 210))
    draw.line([(0, 220), (w, 220)], fill=(0, 240, 255, 255), width=4)

    # Top Header Text
    draw.text((w // 2, 70), "⚡ VOLT REPAIR STUDIO ⚡", font=font_title, fill=(255, 255, 255), anchor="mm")

    # Dynamic Badge
    bbox = draw.textbbox((0, 0), badge_text, font=font_badge)
    bw, bh = bbox[2] - bbox[0] + 40, bbox[3] - bbox[1] + 20
    bx = (w - bw) // 2
    draw.rounded_rectangle([bx, 120, bx + bw, 120 + bh], radius=16, fill=(*badge_color, 240))
    draw.text((w // 2, 120 + bh // 2), badge_text, font=font_badge, fill=(10, 15, 30), anchor="mm")

    # Bottom Footer Background
    draw.rectangle([0, h - 220, w, h], fill=(10, 15, 30, 220))
    draw.line([(0, h - 220), (w, h - 220)], fill=(0, 240, 255, 255), width=4)
    draw.text((w // 2, h - 160), "📲 Agenda por WhatsApp: 720 815 7790", font=font_footer, fill=(255, 230, 0), anchor="mm")
    draw.text((w // 2, h - 100), "🛡️ 90 Días de Garantía | TikTok: @voltrepair32", font=font_badge, fill=(200, 210, 230), anchor="mm")

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
Style: TikTokYellow,Arial Black,50,&H0000FFFF,&H000000FF,&H00000000,&H80000000,-1,0,0,0,100,100,0,0,1,5,2,2,70,70,380,1

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
                if sum(len(x) for x in cur) + len(cur) + len(w) > 30:
                    wrapped.append(" ".join(cur))
                    cur = [w]
                else:
                    cur.append(w)
            if cur:
                wrapped.append(" ".join(cur))
            wrapped_str = r"\N".join(wrapped)
            dialogues.append(f"Dialogue: 0,{start_ass},{end_ass},TikTokYellow,,0,0,0,,{wrapped_str}")
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
    return 25.0

def render_reel(cfg: dict):
    rid = cfg["id"]
    voice_id = cfg["voice_id"]
    print(f"\n=======================================================")
    print(f"🎬 Iniciando Renderizado de: {rid}")
    print(f"=======================================================")

    voice_path = BROLL_DIR / f"{voice_id}_voice.mp3"
    vtt_path = BROLL_DIR / f"{voice_id}_sub.vtt"
    ass_path = BROLL_DIR / f"{voice_id}_sub.ass"
    overlay_path = BROLL_DIR / f"{voice_id}_overlay.png"
    hero_img = BROLL_DIR / cfg["hero_image"]
    broll_vid = BROLL_DIR / cfg["broll_video"]
    bg_music = BROLL_DIR / "bg_music.webm"
    out_mp4 = EXPORT_DIR / f"{rid}.mp4"
    copy_path = EXPORT_DIR / cfg["copy_file"]

    # 1. Overlay
    make_overlay(cfg["badge_text"], cfg["badge_color"], overlay_path)
    # 2. Subtítulos ASS
    convert_vtt_to_ass(vtt_path, ass_path)
    # 3. Guardar texto de redes sociales
    with open(copy_path, "w", encoding="utf-8") as f:
        f.write(cfg["copy_content"])

    # 4. Cálculo de tiempos
    total_dur = get_audio_duration(voice_path) + 0.5
    seg1_dur = 4.5
    seg2_dur = min(cfg["broll_duration"], total_dur - seg1_dur - 4.0)
    seg3_dur = max(4.0, total_dur - seg1_dur - seg2_dur)

    fps = 30
    seg1_frames = int(seg1_dur * fps)
    seg3_frames = int(seg3_dur * fps)
    broll_st = cfg["broll_start"]
    broll_en = broll_st + seg2_dur
    fade_st = max(1.0, total_dur - 2.0)

    filter_complex = f"""
[0:v]loop=loop={seg1_frames}:size=1:start=0,scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,setsar=1,fps={fps}[seg1];
[1:v]trim=start={broll_st}:end={broll_en},setpts=PTS-STARTPTS,scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,setsar=1,fps={fps}[seg2];
[0:v]loop=loop={seg3_frames}:size=1:start=0,scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,setsar=1,fps={fps}[seg3];
[seg1][seg2][seg3]concat=n=3:v=1:a=0[v_concat];
[v_concat][3:v]overlay=0:0[v_over];
[v_over]subtitles={ass_path.name}[v_final];
[2:a]volume=1.0[a_voice];
[4:a]aloop=loop=-1:size=2e+09,volume=0.12,afade=t=out:st={fade_st:.1f}:d=2[a_music];
[a_voice][a_music]amix=inputs=2:duration=first:dropout_transition=2[a_final]
"""

    cmd = [
        FFMPEG, "-y",
        "-i", str(hero_img),
        "-i", str(broll_vid),
        "-i", str(voice_path),
        "-i", str(overlay_path),
        "-i", str(bg_music),
        "-filter_complex", filter_complex.strip(),
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
        print(f"✅ Éxito: {out_mp4.name} ({mb:.2f} MB)")
    else:
        print(f"❌ Error en {rid}:")
        print(res.stderr[-800:])

if __name__ == "__main__":
    for c in REELS_CONFIG:
        render_reel(c)
    print("\n🎉 Todos los reels han sido generados exitosamente en:")
    print(str(EXPORT_DIR))
