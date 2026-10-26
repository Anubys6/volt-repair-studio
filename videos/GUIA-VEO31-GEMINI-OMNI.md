# ⚡ GUÍA OFICIAL: INTEGRACIÓN DE VEO 3.1 Y GEMINI OMNI FLASH
## Automatización de Video Vertical (9:16) para Volt Repair Studio

Esta guía documenta la arquitectura técnica y la integración oficial de **Google Veo 3.1** y **Gemini Omni 1.1 Flash** para la generación de reels virales y clips cinemáticos de reparación de celulares.

---

### 1. La Evolución de Google: De Veo 3.1 a Gemini Omni 1.1 Flash

Al consultar directamente los endpoints anteriores de Google GenAI (`models/veo-3.1-generate-preview`), la API oficial de Google responde:

> *"This model models/veo-3.1-generate-preview is no longer available. Please update your code to use models/gemini-omni-1.1-flash for the latest features and improvements. We recommend you to use the Interactions API."*

Google ha unificado la tecnología de generación de video de **Veo 3.1** dentro del nuevo modelo multimodal **Gemini Omni 1.1 Flash (`gemini-omni-1.1-flash`)**, operado a través de la **Interactions API** del SDK oficial `google-genai`.

---

### 2. Capacidades de Gemini Omni Flash para Reels (9:16)

1. **Relación de Aspecto Vertical Nativa (`9:16`)**:
   Genera video vertical sin recortes ni bandas negras, perfecto para TikTok, Instagram Reels y YouTube Shorts.
2. **Resoluciones Soportadas**:
   - `360p`: `360x640` (rápido para pruebas)
   - `720p`: `720x1280` (estándar HD)
   - `1080p`: `1080x1920` (máxima nitidez vertical)
   - `4K`: `2160x3840` (ultra-alta definición)
3. **Modalidades de Generación**:
   - **Text-to-Video**: Escribir la escena técnica directamente.
   - **First-Frame-to-Video**: Usar una imagen inicial de referencia para que el video empiece desde ese fotograma y continúe en movimiento hiperrealista.
   - **Video-to-Video / Extensiones**: Extender clips existentes hasta 40 segundos.

---

### 3. Cómo Ejecutarlo por Consola / Script

El plugin oficial `gemini-omni-flash-api` incluye el script listo para ejecutar:

```bash
# Generar un clip vertical de 5 segundos a 1080p
python "C:\Users\SAmue\.gemini\config\plugins\gemini-api\skills\gemini-omni-flash-api\scripts\video\generate_video.py" \
  "Macro shot of hands unscrewing pentalobe screws on an iPhone with blue repair mat" \
  --aspect-ratio 9:16 \
  --duration 5 \
  --resolution 1080p \
  --output "C:\Users\SAmue\Desktop\Volt-Repair-Studio\videos\b_roll\omni_clip.mp4"
```

#### A partir de un fotograma de inicio (First Frame):
```bash
python "C:\Users\SAmue\.gemini\config\plugins\gemini-api\skills\gemini-omni-flash-api\scripts\video\generate_video.py" \
  "The technician begins unscrewing the phone with precision screwdriver" \
  --first-frame "C:\Users\SAmue\Desktop\Volt-Repair-Studio\assets\volt_tech_living_room.jpg" \
  --aspect-ratio 9:16 \
  --duration 5 \
  --resolution 1080p \
  --output "C:\Users\SAmue\Desktop\Volt-Repair-Studio\videos\b_roll\tech_in_motion.mp4"
```

---

### 4. Flujo de Producción Híbrido en Volt Repair Studio

Para garantizar la máxima velocidad, estabilidad y cero costos innecesarios, combinamos:
1. **Tomas de Micro-Soldadura y Apertura 4K Reales**: Filmadas con instrumental quirúrgico real (cero alucinaciones de IA en los chips).
2. **Generación con Gemini Omni Flash**: Para planos de transición dinámicos y demostración de herramientas.
3. **Motor de Renderizado Rápido en Local (`render_viral_tech_reels.py`)**: Sincroniza audio, subtítulos cinemáticos en zona segura y música atenuada a 60 fps en segundos.
