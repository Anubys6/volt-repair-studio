# Calculate frame intervals for 17 scenes
# Total frames: 1383 (46.10s * 30 fps)

scenes = [
    # (name, img, start_f, end_f, badge, headline, accent)
    ("01_intro", "stock_congruent/scene_01_intro.jpg", 0, 54, "⚡ VOLT REPAIR STUDIO", "¡QUÉ ONDA AMIGOS!", "#00f0ff"),
    ("02_broken", "stock_congruent/scene_02_broken.jpg", 54, 143, "💥 PANTALLA ROTA", "¿SE TE ESTRELLÓ EL DISPLAY?", "#ff0055"),
    ("03a_plaza", "stock_congruent/scene_03a_plaza.jpg", 143, 203, "⚠️ RIESGO EN PLAZAS", "¡NO LO DEJES DÍAS EN PLAZAS!", "#ffea00"),
    ("03b_privacy", "stock_congruent/scene_03b_privacy.jpg", 203, 263, "🔒 MIEDO POR TUS FOTOS", "¿MIEDO A QUE REVISEN TUS DATOS?", "#ff0055"),
    ("04_arrival", "stock_congruent/scene_04_arrival.jpg", 263, 368, "🚗 SERVICIO A DOMICILIO", "VAMOS DIRECTO A TU CASA U OFICINA", "#00f0ff"),
    ("05a_dining", "stock_congruent/scene_05a_dining.jpg", 368, 437, "🏠 EN TU PROPIO COMEDOR", "REPARAMOS EN TU MESA EN 25 MIN", "#10b981"),
    ("05b_live", "stock_congruent/scene_05b_live.jpg", 437, 505, "👀 TRANSPARENCIA TOTAL", "TODO FRENTE A TUS PROPIOS OJOS", "#ffea00"),
    ("06_pentalobe", "stock_congruent/scene_06_pentalobe.jpg", 505, 619, "🔧 DESMONTAJE DE PRECISIÓN", "QUITAMOS TORNILLOS PENTALOBE", "#00f0ff"),
    ("07_suction", "stock_congruent/scene_07_suction.jpg", 619, 724, "📱 APERTURA CON VENTOSA", "VENTOSA ESPECIAL: CERO RAYONES", "#00f0ff"),
    ("08_battery", "stock_congruent/scene_08_battery.jpg", 724, 836, "⚡ SEGURIDAD EN CIRCUITOS", "DESCONECTAMOS BATERÍA AL INSTANTE", "#ff0055"),
    ("09a_truetone", "stock_congruent/scene_09a_truetone.jpg", 836, 892, "🔬 PROGRAMADORA JCID", "TRANSFERENCIA DE SERIALES TRUE TONE", "#a855f7"),
    ("09b_eeprom", "stock_congruent/scene_09b_eeprom.jpg", 892, 949, "✨ 120 HERTZ Y COLOR", "CONSERVAMOS FLUIDEZ Y TONOS DE FÁBRICA", "#ffea00"),
    ("10_display", "stock_congruent/scene_10_new_display.jpg", 949, 1054, "🛡️ REFACCIÓN CERTIFICADA", "PANTALLA OLED GRADO A PLUS", "#10b981"),
    ("11_touch", "stock_congruent/scene_11_touch_test.jpg", 1054, 1154, "📱 PRUEBA MULTITOUCH", "TEST DE TOUCH Y SENSORES CONTIGO", "#00f0ff"),
    ("12a_price", "stock_congruent/scene_12a_pricing.jpg", 1154, 1223, "💵 TARIFA FIJA TRANSPARENTE", "SOLO $700 DE MANO DE OBRA", "#10b981"),
    ("12b_warranty", "stock_congruent/scene_12b_warranty.jpg", 1223, 1292, "🛡️ RESPALDO TOTAL", "90 DÍAS DE GARANTÍA POR ESCRITO", "#ffea00"),
    ("13_whatsapp", "stock_congruent/scene_13_whatsapp.jpg", 1292, 1383, "📲 AGENDA HOY MISMO", "¡MÁNDANOS WHATSAPP Y COTIZA YA!", "#00f0ff"),
]

for s in scenes:
    dur = s[3] - s[2]
    dur_sec = dur / 30.0
    print(f"{s[0]:12} | F{s[2]:4d} -> F{s[3]:4d} ({dur:3d} frames, {dur_sec:4.2f}s) | {s[4]}")
print(f"Total frames: {scenes[-1][3]} ({scenes[-1][3]/30.0:.2f}s)")
