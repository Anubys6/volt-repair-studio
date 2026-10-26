# ⚡ GUÍA MAESTRA: VIDEOS VERTICALES (9:16) ULTRA-REALISTAS CON GOOGLE GEMINI Y FLOW
## Metodología Aprendida del Tutorial de Eldrin Lobo aplicada a Volt Repair Studio

Esta guía documenta con precisión quirúrgica el método revelado en el tutorial de YouTube (*"Cómo Hacer Videos VERTICALES con Gemini - El Truco que Funciona"*) y cómo lo implementamos en **Volt Repair Studio** para dominar TikTok ([@voltrepair32](https://www.tiktok.com/@voltrepair32)), Instagram Reels ([@voltrepair.mx](https://www.instagram.com/voltrepair.mx/)) y Facebook.

---

## 1. EL TRUCO SECRETO DE GOOGLE GEMINI (Bypass de Aspect Ratio)

### El Problema
En la interfaz web de Google Gemini ([gemini.google.com](https://gemini.google.com/)), la herramienta oficial **"Crear Video"** (alimentada por Google Veo) **NO cuenta con un botón para seleccionar formato vertical (9:16)**. Por defecto, siempre genera video horizontal panorámico (16:9). Si en el prompt escribes *"hazlo vertical"*, *"formato 9:16"* o *"para TikTok"*, el modelo ignora la instrucción de dimensiones.

### La Solución Descubierta en el Tutorial (El Truco)
Gemini activa internamente una canalización de generación condicionada por fotograma (Image-to-Video). Si le envías una imagen con proporción 9:16 antes del prompt, el motor de Veo **hereda forzosamente las dimensiones del archivo adjunto**:

1. **La Semilla Transparente**:
   Creamos un archivo PNG transparente de resolución **1080x1920 píxeles** con canal alfa en cero:
   - Archivo listo para usar en tu sistema: `C:\Users\SAmue\Desktop\Volt-Repair-Studio\videos\aspect_ratio_seed_9_16.png`
2. **Paso a paso en Gemini**:
   - Entra a [gemini.google.com](https://gemini.google.com/).
   - Haz clic en el botón `+` (**Subir archivos / Añadir imagen**).
   - Sube `aspect_ratio_seed_9_16.png` (o una foto 9:16 del técnico de Volt).
   - Haz clic en **Herramientas** y activa **"Crear Video"**.
   - Pega tu prompt de marketing en lenguaje natural (ver plantillas abajo).
   - ¡Listo! Google Veo generará el video en formato **Vertical 9:16 nativo (1080x1920)** sin bordes negros ni recortes.

---

## 2. MÉTODO ALTERNATIVO: GOOGLE FLOW (Google Labs)

En **Google Flow** ([labs.google/flow](https://labs.google/flow)) el control es directo y nativo:

1. Inicia sesión con tu cuenta de Google.
2. Inicia un nuevo proyecto y selecciona la pestaña **"Video"**.
3. En la barra inferior, haz clic en **"Fotogramas o Ingredientes"** (Ingredients).
4. Configura:
   - **Medida / Relación de Aspecto:** `Vertical (9:16)`
   - **Modelo de IA:** `Veo 3.1 Light` (o Veo 3.1 Fast)
   - **Cantidad:** `1 video por prompt`
5. Pega el prompt estructurado y haz clic en **Generar**.
6. Descarga el video en máxima resolución MP4 listo para redes sociales.

---

## 3. FÓRMULA DE PROMPT DE ALTA CONVERSIÓN (UGC Spokesperson)

El tutorial demuestra que los videos que más ventas generan no son renders abstractos ni animaciones con voz sintética, sino el formato **UGC (User Generated Content)**: una persona real hablándole de frente a la cámara con lenguaje cotidiano y honesto.

### Estructura de 4 Capas del Prompt:
1. **Sujeto & Apariencia:** Técnico joven mexicano (23-25 años), playera polo negra con logo sutil "VOLT", postura relajada y mirada fija al lente.
2. **Entorno & Contexto:** Sala iluminada del cliente (para servicio a domicilio) o mesa de microelectrónica con microscopio y esterilla antiestática.
3. **Acción & Demostración:** Sosteniendo el iPhone, mostrando las herramientas de precisión, la programadora EEPROM o las tiras adhesivas de batería.
4. **Diálogo Natural & Hook Directo:** 
   - *Gancho:* "¿Qué onda mi gente? Andamos cambiando pantallas..."
   - *Solución:* "...en tu sala en 25 minutos, sin que nadie revise tus fotos."
   - *Llamado a la acción (CTA):* "Comenta PANTALLA y te paso la cotización de volada."

---

## 4. BANCO DE PROMPTS LISTOS PARA COPIAR Y PEGAR EN GEMINI / FLOW

### 📱 PROMPT 1: Pantalla a Domicilio ($700 Mano de Obra)
```text
Un video vertical 9:16 hiperrealista estilo UGC de TikTok. Un técnico mexicano de 24 años amable y profesional, con playera polo negra con logo discreto 'VOLT', habla directamente a la cámara frontal sosteniendo un iPhone con la pantalla recién cambiada e impecable. Está sentado en la mesa de comedor de una sala moderna y luminosa, con un estuche de destornilladores de precisión abierto a un lado. Mira sonriente al lente y gesticula con naturalidad diciendo con sincronización labial perfecta: '¿Qué onda mi gente? Andamos cambiando pantallas de iPhone a domicilio. En tu propia sala, en 25 minutos y sin borrar absolutamente nada de tu información. Mano de obra de solo 700 pesos. Comenta PANTALLA o mándame WhatsApp y te cotizo de volada.' Iluminación natural de día, profundidad de campo cinematográfica, 4K ultra nítido.
```

### 🔬 PROMPT 2: Programación EEPROM True Tone ($700 Mano de Obra)
```text
Un video vertical 9:16 ultra-realista grabado en primer plano vertical. Un técnico mexicano joven con playera polo negra y logo 'VOLT' en el pecho, en su laboratorio de microelectrónica con un microscopio trinocular estéreo de fondo. Sostiene en una mano una pantalla de iPhone y en la otra una máquina programadora de micro-chips EEPROM portátil con pantalla digital iluminada. Mira directo al espectador con expresión de confianza y gesticula con sincronización labial diciendo: '¿Por qué cuando te cambian la pantalla en las plazas se pierde el brillo automático y el True Tone? Porque no usan programadora. Nosotros transferimos el chip original para conservar los colores de fábrica y los 120 Hertz. Mano de obra de solo 700 pesos. Comenta TRUETONE y te reviso tu equipo hoy mismo.' Tomas nítidas, destellos limpios de instrumental de precisión.
```

### 🔋 PROMPT 3: Batería y Tiras Térmicas OEM ($500 Mano de Obra)
```text
Un video vertical 9:16 estilo reel de redes sociales. Un técnico de reparación de celulares mexicano de 25 años en su taller sobre un tapete antiestático azul. Muestra en primer plano hacia la cámara las tiras adhesivas de extracción elástica originales de una batería nueva de iPhone, y luego muestra el chasis limpio sin pegamento genérico. Habla con sinceridad y carisma mirando al lente diciendo: '¿Sabías que en muchos talleres pegan las baterías con cinta doble cara escolar? Eso daña tu pantalla por sobrecalentamiento. En Volt usamos tiras térmicas elásticas originales de fábrica para dejar tu salud al 100%. Mano de obra de solo 500 pesos. Comenta BATERIA y te agendo tu cambio en 20 minutos.' Enfoque nítido en el producto, iluminación suave de estudio, estilo creador de contenido tech.
```

---

## 5. RECURSOS GENERADOS EN TU SISTEMA
- **Semilla 9:16 Transparente:** `[aspect_ratio_seed_9_16.png](file:///C:/Users/SAmue/Desktop/Volt-Repair-Studio/videos/aspect_ratio_seed_9_16.png)`
- **Página de Lanzamiento y Vista Previa:** `[reels-promocionales.html](file:///C:/Users/SAmue/Desktop/Volt-Repair-Studio/videos/reels-promocionales.html)`
- **Panel de Control Principal:** `[panel-control.html](file:///C:/Users/SAmue/Desktop/Volt-Repair-Studio/panel-control.html)`
