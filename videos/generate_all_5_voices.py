import asyncio
import edge_tts
import imageio_ffmpeg
import subprocess
import json
from pathlib import Path

BASE_DIR = Path(r"C:\Users\SAmue\Desktop\Volt-Repair-Studio")
PUBLIC_DIR = BASE_DIR / "remotion_reels" / "public"
ffmpeg_exe = imageio_ffmpeg.get_ffmpeg_exe()

REELS_SPEECH = {
    4: [
        ("scene_01", "¡Qué onda amigos!", "⚡ VOLT REPAIR STUDIO", "¡QUÉ ONDA AMIGOS!", "#00f0ff", "render-servicio-domicilio", "technician smartphone repair"),
        ("scene_02", "¿Se te estrelló el cristal trasero de tu celular?", "💥 TAPA TRASERA ROTA", "¿CRISTAL TRASERO ESTRELLADO?", "#ff0055", "broken glass smartphone", "broken smartphone glass back"),
        ("scene_03", "¡Mucho cuidado si lo llevas a talleres donde usan pistola de calor!", "⚠️ PISTOLA DE CALOR 300°C", "¡PELIGRO CON PISTOLAS DE CALOR!", "#ffea00", "heat gun repair", "hot air rework station"),
        ("scene_04", "Ese calor extremo derrite los sellos de la cámara...", "📷 SELLOS DERRETIDOS", "EL CALOR ARRUINA TUS CÁMARAS", "#ff0055", "camera sensor phone", "smartphone camera sensor"),
        ("scene_05", "...deforma la batería interna y puede provocar un corto circuito.", "🔥 RIESGO EN BATERÍA", "PELIGRO DE CORTO O EXPLOSIÓN", "#ff0055", "swollen battery", "lithium battery failure"),
        ("scene_06", "¡En Volt Repair Studio tenemos tecnología láser de fibra óptica!", "⚡ MÁQUINA LÁSER", "TECNOLOGÍA LÁSER DE PRECISIÓN", "#00f0ff", "render-maquina-laser", "fiber laser engraving"),
        ("scene_07", "El rayo láser quema el pegamento epóxico sin tocar el chasis metálico...", "🔬 RAYO LÁSER FRÍO", "DESINTEGRA EL PEGAMENTO SIN CALOR", "#a855f7", "laser beam metal", "fiber laser cutting"),
        ("scene_08", "...manteniendo tus cámaras y tu tarjeta madre completamente frías.", "🛡️ CERO CALOR EN PLACA", "CÁMARAS Y CIRCUITOS SEGUROS", "#10b981", "logic board pcb", "smartphone motherboard"),
        ("scene_09", "Retiramos los cristales rotos sin palanquear ni rayar el marco.", "📱 EXTRACCIÓN LIMPIA", "RETIRAMOS CRISTALES SIN RAYONES", "#00f0ff", "precision pry tool", "spudger opening phone"),
        ("scene_10", "Instalamos vidrio trasero templado de calidad original de fábrica.", "💎 TAPA NUEVA OEM", "CRISTAL TEMPLADO ORIGINAL", "#10b981", "new glass back phone", "smartphone back cover"),
        ("scene_11", "Aplicamos prensa de sellado hermético para que no le entre polvo.", "🔧 PRENSA HERMÉTICA", "SELLADO IMPERMEABLE DE FÁBRICA", "#ffea00", "screen clamp repair", "phone repair clamp"),
        ("scene_12", "Tu celular queda como nuevo, sin desarmes riesgosos ni calor.", "✨ RESULTADO IMPECABLE", "TU TELÉFONO COMO NUEVO", "#10b981", "clean smartphone back", "finished smartphone repair"),
        ("scene_13", "Mano de obra fija de solo 500 pesitos con 90 días de garantía por escrito.", "💵 TARIFA FIJA $500", "SOLO $500 DE MANO DE OBRA", "#10b981", "warranty certificate", "written warranty document"),
        ("scene_14", "¡Mándanos un WhatsApp hoy mismo y te cotizo de volada!", "📲 AGENDA HOY MISMO", "¡MÁNDANOS WHATSAPP Y COTIZA YA!", "#00f0ff", "logo-volt-studio", "whatsapp icon message")
    ],
    5: [
        ("scene_01", "¡Qué onda amigos!", "⚡ VOLT REPAIR STUDIO", "¡QUÉ ONDA AMIGOS!", "#00f0ff", "render-servicio-domicilio", "technician smartphone repair"),
        ("scene_02", "¿Tu teléfono ya no agarra carga o tienes que doblar el cable para que conecte?", "🔌 NO AGARRA CARGA", "¿BATALLAS PARA QUE CARGUE?", "#ff0055", "usb c cable phone", "smartphone charging cable"),
        ("scene_03", "¡No caigas en la trampa de los talleres que te cobran 800 pesos por cambiar el puerto!", "❌ ESTAFAS EN CALLE", "NO PAGUES $800 POR CAMBIO DE PUERTO", "#ffea00", "repair shop scam", "cluttered phone repair shop"),
        ("scene_04", "¡El noventa por ciento de las veces tu centro de carga está completamente sano!", "📱 PUERTO EN BUEN ESTADO", "¡TU CENTRO DE CARGA ESTÁ SANO!", "#10b981", "usb c port macro", "smartphone charging port"),
        ("scene_05", "Lo único que pasa es que se llena de pelusa de pantalón compactada al fondo.", "⚠️ PELUSA COMPACTADA", "PELUSA DE BOLSILLO AL FONDO", "#ff0055", "pocket lint close up", "dust in connector"),
        ("scene_06", "Cada vez que conectas el cargador, aplastas más la suciedad y el conector no baja.", "📉 FALSO CONTACTO", "EL CONECTOR CHOCA CON LA PELUSA", "#ffea00", "usb c connector plug", "lightning cable plug"),
        ("scene_07", "¡En Volt Repair Studio te lo revisamos en tu propia sala!", "🏠 SERVICIO EN TU COMEDOR", "REVISIÓN EN TU SALA EN 15 MIN", "#00f0ff", "living room desk repair", "technician at home"),
        ("scene_08", "Usamos microscopio óptico y pinzas no conductoras de titanio.", "🔬 MICROSCOPIO ÓPTICO", "INSTRUMENTAL ANTIESTÁTICO FINO", "#a855f7", "stereo microscope repair", "precision tweezers electronics"),
        ("scene_09", "Extraemos toda la pelusa en dos minutos sin doblar los pines de cobre.", "✨ LIMPIEZA PROFUNDA", "EXTRACCIÓN SIN DOBLAR PINES", "#10b981", "copper contact pins", "clean circuit contacts"),
        ("scene_10", "Conectamos nuestro tester USB digital para medir el amperaje exacto de carga rápida.", "⚡ TESTER USB DIGITAL", "MEDICIÓN DE VOLTAJE Y AMPERAJE", "#00f0ff", "usb tester meter", "digital voltmeter display"),
        ("scene_11", "Honestidad total: solo te cobramos una limpieza básica y no te inventamos fallas.", "💎 HONESTIDAD TOTAL", "SOLO COBRAMOS LIMPIEZA BÁSICA", "#10b981", "honest repair service", "happy customer smartphone"),
        ("scene_12", "Garantía de 90 días por escrito y tu teléfono cargando al cien.", "🛡️ RESPALDO ESCRITO", "GARANTÍA DE 90 DÍAS POR ESCRITO", "#ffea00", "fast charging indicator", "phone charging 100 percent"),
        ("scene_13", "¡Mándanos un WhatsApp hoy mismo y te cotizo de volada!", "📲 AGENDA HOY MISMO", "¡MÁNDANOS WHATSAPP Y COTIZA YA!", "#00f0ff", "logo-volt-studio", "whatsapp icon support")
    ],
    6: [
        ("scene_01", "¡Qué onda amigos!", "⚡ VOLT REPAIR STUDIO", "¡QUÉ ONDA AMIGOS!", "#00f0ff", "render-servicio-domicilio", "technician smartphone repair"),
        ("scene_02", "¿Te dijeron en la plaza que el Face ID de tu iPhone ya no tiene solución?", "🔒 FACE ID DESACTIVADO", "¿TE DIJERON QUE YA NO SIRVE?", "#ff0055", "face id not working", "face id disabled screen"),
        ("scene_03", "¡Eso te dicen porque no saben de microelectrónica avanzada!", "❌ FALTA DE TÉCNICA", "NO SABEN DE MICROELECTRÓNICA", "#ffea00", "bad soldering pcb", "messy electronics bench"),
        ("scene_04", "Cuando cambian una pantalla a la fuerza, rasgan el flexor del sensor Dot Projector.", "⚠️ FLEXOR RASGADO", "ROMPEN EL SENSOR DOT PROJECTOR", "#ff0055", "torn flex ribbon cable", "damaged phone ribbon"),
        ("scene_05", "Ese microchip emite treinta mil puntos infrarrojos invisibles para reconocer tu cara.", "🔬 30,000 PUNTOS LÁSER", "EMITE 30,000 PUNTOS INFRARROJOS", "#a855f7", "infrared dot projector", "facial recognition sensor"),
        ("scene_06", "¡Si se rompe el flexor, Apple bloquea la biometría por seguridad!", "🛡️ BLOQUEO BIOMÉTRICO", "BLOQUEO DE SEGURIDAD BIOMÉTRICA", "#ff0055", "security lock chip", "biometric secure enclave"),
        ("scene_07", "¡En Volt Repair Studio hacemos micro-cirugía bajo microscopio!", "💎 MICRO-CIRUGÍA", "REPARACIÓN BAJO MICROSCOPIO", "#00f0ff", "render-equipo-microsoldadura", "microscope soldering lab"),
        ("scene_08", "Retiramos el prisma de cristal con cautín de alta frecuencia sin quemar el diodo.", "🔧 CAUTÍN DE ALTA FRECUENCIA", "EXTRACCIÓN TÉRMICA DE PRECISIÓN", "#ffea00", "fine tip soldering iron", "jbc soldering micro"),
        ("scene_09", "Soldamos un puente de micro-alambre de plata más delgado que un cabello humano.", "🔬 MICRO-JUMPERS DE PLATA", "PUENTES MÁS DELGADOS QUE UN CABELLO", "#a855f7", "jumper wire microscope", "micro soldering wire pcb"),
        ("scene_10", "Trasplantamos el circuito original a un nuevo flexor programable JCID.", "⚡ TRASPLANTE DE CHIP", "NUEVO FLEXOR PROGRAMABLE JCID", "#00f0ff", "jcid face id tag-on", "eeprom programmer board"),
        ("scene_11", "Probamos el haz infrarrojo en nuestra cámara especial contigo presente.", "✨ PRUEBA INFRARROJA", "TEST DE HAZ INFRARROJO EN VIVO", "#10b981", "infrared camera light", "ir emitter testing"),
        ("scene_12", "Tu Face ID vuelve a desbloquear al instante y sin perder tus fotos ni datos.", "📱 DESBLOQUEO AL INSTANTE", "FACE ID RECUPERADO AL 100%", "#10b981", "face unlock smiling", "iphone face id success"),
        ("scene_13", "Mano de obra fija de solo 700 pesitos con 90 días de garantía total por escrito.", "💵 MANO DE OBRA FIJA $700", "90 DÍAS DE GARANTÍA POR ESCRITO", "#ffea00", "warranty certificate", "transparent price invoice"),
        ("scene_14", "¡Mándanos un WhatsApp hoy mismo y recupera tu Face ID!", "📲 AGENDA HOY MISMO", "¡RECUPERA TU FACE ID DE VOLADA!", "#00f0ff", "logo-volt-studio", "whatsapp icon phone")
    ],
    7: [
        ("scene_01", "¡Qué onda amigos!", "⚡ VOLT REPAIR STUDIO", "¡QUÉ ONDA AMIGOS!", "#00f0ff", "render-servicio-domicilio", "technician smartphone repair"),
        ("scene_02", "¿La cámara de tu celular tiembla como loca, zumba como abeja o no enfoca?", "📷 CÁMARA TEMBLOROSA", "¿LA CÁMARA TIEMBLA Y ZUMBA?", "#ff0055", "blurry camera phone", "shaky camera screen"),
        ("scene_03", "¡El noventa por ciento de las veces pasa por poner el cel en el soporte de una moto!", "🏍️ VIBRACIÓN DE MOTO", "CULPA DEL SOPORTE DE LA MOTO", "#ffea00", "motorcycle phone mount", "motorcycle handlebar phone"),
        ("scene_04", "Las vibraciones del motor rompen los electroimanes del estabilizador óptico OIS.", "⚠️ ELECTROIMANES ROTOS", "SE ROMPE EL ESTABILIZADOR OIS", "#ff0055", "ois optical image stabilization", "camera copper coils lens"),
        ("scene_05", "¡Y en los talleres de la calle te ponen cámaras usadas que botan alerta de pieza desconocida!", "❌ CÁMARAS USADAS", "BOTAN ALERTA DE PIEZA DESCONOCIDA", "#ff0055", "unknown part warning", "apple parts service alert"),
        ("scene_06", "¡En Volt Repair Studio lo resolvemos en tu sala en 25 minutos!", "🏠 EN TU PROPIA SALA", "EN TU CASA EN 25 MINUTOS", "#00f0ff", "living room table repair", "mobile technician dining"),
        ("scene_07", "Desarmamos con precisión y retiramos el módulo de cámara dañado.", "🔧 DESMONTAJE SEGURO", "RETIRAMOS EL MÓDULO DAÑADO", "#00f0ff", "camera module disassembly", "triple camera removal"),
        ("scene_08", "Instalamos cámara certificada con lentes de cristal de zafiro de fábrica.", "💎 CRISTAL DE ZAFIRO OEM", "CÁMARA CERTIFICADA DE FÁBRICA", "#10b981", "sapphire camera lens", "new smartphone camera"),
        ("scene_09", "Calibramos el sensor giroscópico y probamos el enfoque macro y zoom contigo presente.", "🔬 CALIBRACIÓN EN VIVO", "TEST DE MACRO Y ZOOM EN VIVO", "#a855f7", "macro focus test", "camera zoom photography"),
        ("scene_10", "Tus videos en 4K vuelven a ser súper estables y cinematográficos.", "✨ VIDEO 4K ULTRA FLUIDO", "VIDEOS ULTRA ESTABLES EN 4K", "#10b981", "smooth cinematic video", "4k video shooting"),
        ("scene_11", "Mano de obra fija de solo 600 pesitos con 90 días de garantía por escrito.", "💵 MANO DE OBRA FIJA $600", "SOLO $600 CON 90 DÍAS GARANTÍA", "#ffea00", "warranty certificate", "fixed pricing card"),
        ("scene_12", "¡Mándanos un WhatsApp hoy mismo y cotiza tu modelo de volada!", "📲 AGENDA HOY MISMO", "¡MÁNDANOS WHATSAPP Y COTIZA YA!", "#00f0ff", "logo-volt-studio", "whatsapp message chat")
    ],
    8: [
        ("scene_01", "¡Qué onda amigos!", "⚡ VOLT REPAIR STUDIO", "¡QUÉ ONDA AMIGOS!", "#00f0ff", "render-servicio-domicilio", "technician smartphone repair"),
        ("scene_02", "¡Por favor nunca en la vida metas tu celular en arroz si se te cayó al agua!", "🍚 EL MITO DEL ARROZ", "¡NUNCA METAS TU CEL EN ARROZ!", "#ff0055", "phone in rice bowl", "wet phone white rice"),
        ("scene_03", "¡El arroz es el peor enemigo de la electrónica y te va a costar miles de pesos!", "❌ PEOR ENEMIGO", "TE VA A COSTAR MILES DE PESOS", "#ffea00", "damaged electronics rice", "rice grains dirty phone"),
        ("scene_04", "El arroz no absorbe el agua atrapada debajo de los blindajes metálicos soldados.", "⚠️ AGUA ATRAPADA", "EL AGUA SIGUE BAJO LOS BLINDAJES", "#ff0055", "emi shield circuit water", "water droplets on pcb"),
        ("scene_05", "Al contrario: suelta almidón en polvo que se mezcla con el agua y acelera la corrosión.", "🧪 ALMIDÓN CORROSIVO", "EL ALMIDÓN ACELERA LA CORROSIÓN", "#ff0055", "green corrosion circuit", "corroded motherboard pcb"),
        ("scene_06", "En cuestión de horas, la salinidad pudre las pistas de cobre y quema el procesador.", "🔥 PISTAS PODRIDAS", "PUDRE PISTAS Y QUEMA EL CHIP", "#ff0055", "burned cpu chip", "microscope corroded traces"),
        ("scene_07", "¡Si tu celular se moja, lo primero que debes hacer es apagarlo y no conectarlo!", "⚡ APÁGALO DE INMEDIATO", "¡APÁGALO Y NO LO CONECTES!", "#00f0ff", "power off phone switch", "do not charge warning"),
        ("scene_08", "¡Llámanos a Volt Repair Studio para hacer un rescate químico inmediato!", "🚗 RESCATE QUÍMICO", "RESCATE QUÍMICO A DOMICILIO", "#00f0ff", "mobile technician emergency", "service van technician"),
        ("scene_09", "Desmontamos blindajes y sumergimos la placa en tina ultrasónica con alcohol al 99%.", "🔬 TINA ULTRASONICA 99%", "TINA ULTRASÓNICA CON ISOPROPÍLICO", "#a855f7", "ultrasonic cleaner pcb", "pcb cleaning tank"),
        ("scene_10", "Las ondas de cavitación eliminan todo el sulfato y minerales sin tocar los componentes.", "✨ ONDAS DE CAVITACIÓN", "ELIMINA SULFATO Y MINERALES", "#10b981", "ultrasonic cavitation bubbles", "cleaned circuit board shiny"),
        ("scene_11", "Aplicamos secado térmico controlado y medimos con multímetro que no haya cortos.", "🔧 SECADO Y MULTÍMETRO", "SECADO CONTROLADO Y CERO CORTOS", "#ffea00", "multimeter test pcb", "heat rework board drying"),
        ("scene_12", "Salvamos tu tarjeta madre y tus fotos con mano de obra de solo 500 pesitos.", "💎 SALVAMOS TUS FOTOS", "SALVAMOS TUS DATOS POR $500", "#10b981", "happy client working phone", "recovered photos screen"),
        ("scene_13", "¡Mándanos un WhatsApp de emergencia y te atendemos de volada!", "📲 AGENDA HOY MISMO", "¡MÁNDANOS WHATSAPP DE VOLADA!", "#00f0ff", "logo-volt-studio", "whatsapp urgent chat")
    ]
}

async def generate_speech_for_all():
    results = {}
    for reel_id, scenes in REELS_SPEECH.items():
        full_text = " ".join([s[1] for s in scenes])
        audio_name = f"volt_voice_reel{reel_id}.mp3"
        audio_path = PUBLIC_DIR / audio_name
        
        c = edge_tts.Communicate(full_text, "es-US-AlonsoNeural", rate="+10%")
        boundaries = []
        with open(audio_path, "wb") as f:
            async for chunk in c.stream():
                if chunk["type"] == "audio":
                    f.write(chunk["data"])
                elif chunk["type"] == "SentenceBoundary":
                    boundaries.append(chunk)

        res = subprocess.run([ffmpeg_exe, "-i", str(audio_path)], stderr=subprocess.PIPE, text=True)
        total_dur = 0.0
        for line in res.stderr.splitlines():
            if "Duration:" in line:
                parts = line.split("Duration:")[1].split(",")[0].strip().split(":")
                total_dur = float(parts[0])*3600 + float(parts[1])*60 + float(parts[2])
                break

        print(f"Reel {reel_id}: Generated {audio_name} -> {total_dur:.2f}s ({int(total_dur*30)} frames), {len(boundaries)} boundaries")
        results[reel_id] = {
            "duration_sec": total_dur,
            "duration_frames": int(total_dur * 30),
            "audio_file": audio_name,
            "boundaries": boundaries
        }
    
    with open(VIDEOS_DIR / "reels_speech_metadata.json", "w", encoding="utf-8") as f:
        # Convert boundaries to plain dicts
        serializable = {}
        for rid, d in results.items():
            serializable[rid] = {
                "duration_sec": d["duration_sec"],
                "duration_frames": d["duration_frames"],
                "audio_file": d["audio_file"],
                "boundaries": [
                    {"offset": b["offset"], "duration": b["duration"], "text": b["text"]}
                    for b in d["boundaries"]
                ]
            }
        json.dump(serializable, f, indent=2, ensure_ascii=False)
    print("Speech generation for all 5 reels finished!")

if __name__ == "__main__":
    asyncio.run(generate_speech_for_all())
