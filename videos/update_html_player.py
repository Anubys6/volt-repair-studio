from pathlib import Path

html_path = Path(r"C:\Users\SAmue\Desktop\Volt-Repair-Studio\videos\reels-promocionales.html")
content = html_path.read_text(encoding="utf-8")

old_cards_marker = '<!-- LISTA DE LOS 3 REELS -->'
new_cards = '''<!-- LISTA DE REELS -->
      <div class="video-card-item active" id="card5" onclick="loadReel(5)" style="border-color: #00f0ff; background: rgba(0, 240, 255, 0.15); box-shadow: 0 0 20px rgba(0, 240, 255, 0.25);">
        <h4>
          <span>🌟 5. Reel Congruente + Voz Amistosa (17 Escenas)</span>
          <span style="font-size: 0.8rem; color: var(--cyan); font-weight: 900;">⭐ MASTER OFICIAL</span>
        </h4>
        <p>17 cortes visuales rápidos sincronizados palabra por palabra con la locución cálida y amistosa. Zoom continuo Ken Burns en cada segundo y congruencia 1:1 entre audio y video.</p>
      </div>'''

if old_cards_marker in content:
    content = content.replace(old_cards_marker, f"{old_cards_marker}\n      {new_cards}")
    # Remove 'active' from card1
    content = content.replace('<div class="video-card-item active" id="card1"', '<div class="video-card-item" id="card1"')

# Add entry 5 to reelsData
old_reels_data_end = '    };\n\n    let currentReelId = 1;'
new_reels_data_entry = ''',
      5: {
        video: "reels_exportados/reel_remotion_congruente_amigable_1080x1920.mp4",
        copy: `⚡ ¡Qué onda amigos! ¿Se te estrelló la pantalla de tu celular? 📱💥

¡No lo dejes días enteros en las plazas con miedo a que revisen tus fotos o cambien piezas! En Volt Repair Studio vamos directo a tu domicilio y en 25 minutos cambiamos tu display frente a tus propios ojos en tu propio comedor.

🔧 Desmontaje milimétrico con desarmadores pentalobe
📱 Apertura con ventosa especial (cero rayones en el marco)
⚡ Desconexión de batería inmediata para proteger circuitos
🔬 Programadora JCID de microchips para transferir True Tone y 120Hz
🛡️ Refacción certificada Grado A+ con colores idénticos de fábrica
✨ Pruebas de multitouch y sensores en vivo contigo presente
💵 Mano de obra fija transparente: Solo $700 pesitos
📝 90 días de garantía total por escrito

📲 ¡Mándanos un WhatsApp hoy mismo y te cotizo de volada!
WhatsApp: +52 1 720 815 7790
🌐 Sitio Oficial: https://anubys6.github.io/volt-repair-studio/
🎵 TikTok: https://www.tiktok.com/@voltrepair32

#voltrepair32 #VoltRepairStudio #ReparacionDeCelulares #iPhoneMexico #ReparacionADomicilio #PantallaRota #ManoDeObraTransparente #TrueTone`
      }
    };

    let currentReelId = 5;'''

if old_reels_data_end in content:
    content = content.replace(old_reels_data_end, new_reels_data_entry)
else:
    # Try with \r\n
    old_reels_data_end_crlf = '    };\r\n\r\n    let currentReelId = 1;'
    if old_reels_data_end_crlf in content:
        content = content.replace(old_reels_data_end_crlf, new_reels_data_entry)

# Update initial load
content = content.replace("loadReel(1);", "loadReel(5);")

html_path.write_text(content, encoding="utf-8")
print("reels-promocionales.html updated successfully with Card 5!")
