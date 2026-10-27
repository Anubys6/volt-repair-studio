import React from "react";
import {
  AbsoluteFill,
  Audio,
  Img,
  interpolate,
  Sequence,
  spring,
  staticFile,
  useCurrentFrame,
  useVideoConfig,
} from "remotion";

interface SceneConfig {
  from: number;
  durationInFrames: number;
  img: string;
  badge: string;
  headline: string;
  accent: string;
}

const SCENES: SceneConfig[] = [
  {
    from: 0,
    durationInFrames: 54, // 0.0s - 1.80s
    img: "stock_congruent/scene_01_intro.jpg",
    badge: "⚡ VOLT REPAIR STUDIO",
    headline: "¡QUÉ ONDA AMIGOS!",
    accent: "#00f0ff",
  },
  {
    from: 54,
    durationInFrames: 89, // 1.80s - 4.77s
    img: "stock_congruent/scene_02_broken.jpg",
    badge: "💥 PANTALLA ESTRELLADA",
    headline: "¿SE TE ROMPIÓ EL DISPLAY?",
    accent: "#ff0055",
  },
  {
    from: 143,
    durationInFrames: 60, // 4.77s - 6.77s
    img: "stock_congruent/scene_03a_plaza.jpg",
    badge: "⚠️ RIESGO EN PLAZAS",
    headline: "¡NO LO DEJES DÍAS EN TALLERES!",
    accent: "#ffea00",
  },
  {
    from: 203,
    durationInFrames: 60, // 6.77s - 8.77s
    img: "stock_congruent/scene_03b_privacy.jpg",
    badge: "🔒 PRIVACIDAD EN RIESGO",
    headline: "¿MIEDO A QUE REVISEN TUS FOTOS?",
    accent: "#ff0055",
  },
  {
    from: 263,
    durationInFrames: 105, // 8.77s - 12.27s
    img: "stock_congruent/scene_04_arrival.jpg",
    badge: "🚗 SERVICIO A DOMICILIO",
    headline: "VAMOS DIRECTO A TU CASA U OFICINA",
    accent: "#00f0ff",
  },
  {
    from: 368,
    durationInFrames: 69, // 12.27s - 14.57s
    img: "stock_congruent/scene_05a_dining.jpg",
    badge: "🏠 EN TU PROPIO COMEDOR",
    headline: "EN TU MESA EN 25 MINUTOS",
    accent: "#10b981",
  },
  {
    from: 437,
    durationInFrames: 68, // 14.57s - 16.83s
    img: "stock_congruent/scene_05b_live.jpg",
    badge: "👀 TRANSPARENCIA TOTAL",
    headline: "TODO ANTE TUS PROPIOS OJOS",
    accent: "#ffea00",
  },
  {
    from: 505,
    durationInFrames: 114, // 16.83s - 20.63s
    img: "stock_congruent/scene_06_pentalobe.jpg",
    badge: "🔧 DESMONTAJE DE PRECISIÓN",
    headline: "QUITAMOS TORNILLOS PENTALOBE",
    accent: "#00f0ff",
  },
  {
    from: 619,
    durationInFrames: 105, // 20.63s - 24.13s
    img: "stock_congruent/scene_07_suction.jpg",
    badge: "📱 APERTURA CON VENTOSA",
    headline: "VENTOSA ESPECIAL: CERO RAYONES",
    accent: "#00f0ff",
  },
  {
    from: 724,
    durationInFrames: 112, // 24.13s - 27.87s
    img: "stock_congruent/scene_08_battery.jpg",
    badge: "⚡ SEGURIDAD EN CIRCUITOS",
    headline: "DESCONECTAMOS BATERÍA AL INSTANTE",
    accent: "#ff0055",
  },
  {
    from: 836,
    durationInFrames: 56, // 27.87s - 29.73s
    img: "stock_congruent/scene_09a_truetone.jpg",
    badge: "🔬 PROGRAMADORA JCID",
    headline: "TRANSFERENCIA DE TRUE TONE",
    accent: "#a855f7",
  },
  {
    from: 892,
    durationInFrames: 57, // 29.73s - 31.63s
    img: "stock_congruent/scene_09b_eeprom.jpg",
    badge: "✨ FLUIDEZ Y TONOS",
    headline: "CONSERVAMOS 120HZ Y COLOR ORIGINAL",
    accent: "#ffea00",
  },
  {
    from: 949,
    durationInFrames: 105, // 31.63s - 35.13s
    img: "stock_congruent/scene_10_new_display.jpg",
    badge: "🛡️ REFACCIÓN CERTIFICADA",
    headline: "PANTALLA OLED GRADO A PLUS",
    accent: "#10b981",
  },
  {
    from: 1054,
    durationInFrames: 100, // 35.13s - 38.47s
    img: "stock_congruent/scene_11_touch_test.jpg",
    badge: "📱 PRUEBA DE MULTITOUCH",
    headline: "TEST DE TOUCH Y SENSORES EN VIVO",
    accent: "#00f0ff",
  },
  {
    from: 1154,
    durationInFrames: 69, // 38.47s - 40.77s
    img: "stock_congruent/scene_12a_pricing.jpg",
    badge: "💵 MANO DE OBRA FIJA",
    headline: "SOLO $700 DE MANO DE OBRA",
    accent: "#10b981",
  },
  {
    from: 1223,
    durationInFrames: 69, // 40.77s - 43.07s
    img: "stock_congruent/scene_12b_warranty.jpg",
    badge: "🛡️ RESPALDO TOTAL",
    headline: "90 DÍAS DE GARANTÍA POR ESCRITO",
    accent: "#ffea00",
  },
  {
    from: 1292,
    durationInFrames: 91, // 43.07s - 46.10s
    img: "stock_congruent/scene_13_whatsapp.jpg",
    badge: "📲 AGENDA HOY MISMO",
    headline: "¡MÁNDANOS WHATSAPP Y COTIZA YA!",
    accent: "#00f0ff",
  },
];

// Componente individual de cada escena con movimiento continuo Ken Burns
const SceneSlide: React.FC<{
  scene: SceneConfig;
  index: number;
}> = ({ scene, index }) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();

  // Movimiento continuo Ken Burns: zoom dinámico del 100% al 116%
  const scale = interpolate(
    frame,
    [0, scene.durationInFrames],
    [1.0, 1.16],
    { extrapolateRight: "clamp" }
  );

  // Desplazamiento cinematográfico alterno
  const translateY = interpolate(
    frame,
    [0, scene.durationInFrames],
    index % 2 === 0 ? [-12, 18] : [18, -12],
    { extrapolateRight: "clamp" }
  );

  // Transición suave de entrada (crossfade de 5 frames)
  const fadeIn = interpolate(frame, [0, 5], [0, 1], {
    extrapolateRight: "clamp",
  });

  // Animación del texto con resorte físico elástico
  const textSpring = spring({
    frame,
    fps,
    config: { damping: 140, mass: 0.55 },
  });

  return (
    <AbsoluteFill style={{ opacity: fadeIn }}>
      {/* Fotografía técnica con movimiento continuo (cero imágenes estáticas) */}
      <AbsoluteFill
        style={{
          transform: `scale(${scale}) translateY(${translateY}px)`,
          transformOrigin: "center center",
        }}
      >
        <Img
          src={staticFile(scene.img)}
          style={{
            width: "100%",
            height: "100%",
            objectFit: "cover",
          }}
        />
      </AbsoluteFill>

      {/* Viñeta cinematográfica oscura para contraste perfecto de texto */}
      <AbsoluteFill
        style={{
          background:
            "linear-gradient(180deg, rgba(6, 9, 17, 0.90) 0%, rgba(6, 9, 17, 0.20) 22%, rgba(6, 9, 17, 0.25) 62%, rgba(6, 9, 17, 0.96) 100%)",
        }}
      />

      {/* Badge de la etapa en movimiento */}
      <div
        style={{
          position: "absolute",
          top: 175,
          left: 0,
          right: 0,
          display: "flex",
          justifyContent: "center",
          transform: `scale(${interpolate(textSpring, [0, 1], [0.7, 1])})`,
        }}
      >
        <div
          style={{
            background: scene.accent,
            color: "#050914",
            padding: "10px 28px",
            borderRadius: 30,
            fontSize: 24,
            fontWeight: 900,
            fontFamily: "Arial Black, sans-serif",
            letterSpacing: 1,
            boxShadow: `0 0 30px ${scene.accent}99`,
          }}
        >
          {scene.badge}
        </div>
      </div>

      {/* Titular cinemático de alto impacto sincronizado con la locución */}
      <div
        style={{
          position: "absolute",
          top: 260,
          left: 45,
          right: 45,
          textAlign: "center",
          transform: `translateY(${interpolate(textSpring, [0, 1], [30, 0])}px)`,
        }}
      >
        <h2
          style={{
            fontSize: 48,
            fontWeight: 900,
            color: "#ffffff",
            textTransform: "uppercase",
            fontFamily: "Arial Black, sans-serif",
            lineHeight: 1.15,
            margin: 0,
            WebkitTextStroke: "6px #000000",
            paintOrder: "stroke fill",
            textShadow: "0 10px 35px rgba(0,0,0,0.95)",
          }}
        >
          {scene.headline}
        </h2>
      </div>
    </AbsoluteFill>
  );
};

export const VoltReel: React.FC = () => {
  const frame = useCurrentFrame();
  const { fps, durationInFrames, width } = useVideoConfig();

  // Animación del header superior
  const headerEntrance = spring({
    frame,
    fps,
    config: { damping: 200, mass: 0.5 },
  });

  // Pulso constante en la caja de llamada a la acción
  const ctaPulse = interpolate(
    Math.sin((frame / fps) * 3.5),
    [-1, 1],
    [0.985, 1.015]
  );

  // Barra de progreso inferior milimétricamente sincronizada
  const progressWidth = interpolate(frame, [0, durationInFrames], [0, width], {
    extrapolateRight: "clamp",
  });

  return (
    <AbsoluteFill style={{ backgroundColor: "#060911" }}>
      {/* 1. SECUENCIA DINÁMICA DE 17 FOTOS TÉCNICAS CONGRUEBTES (RÁPIDO CAMBIO Y MOVIMIENTO CONTINUO) */}
      {SCENES.map((scene, i) => (
        <Sequence
          key={i}
          from={scene.from}
          durationInFrames={scene.durationInFrames}
        >
          <SceneSlide scene={scene} index={i} />
        </Sequence>
      ))}

      {/* 2. HEADER PERMANENTE CON BRANDING OFICIAL */}
      <div
        style={{
          position: "absolute",
          top: 55,
          left: 0,
          right: 0,
          display: "flex",
          justifyContent: "center",
          alignItems: "center",
          gap: 16,
          transform: `translateY(${interpolate(headerEntrance, [0, 1], [-70, 0])}px)`,
          opacity: headerEntrance,
        }}
      >
        <Img
          src={staticFile("logo.jpg")}
          style={{
            width: 68,
            height: 68,
            borderRadius: 16,
            boxShadow: "0 0 25px rgba(0, 240, 255, 0.7)",
            border: "2px solid #00f0ff",
          }}
        />
        <div>
          <h1
            style={{
              margin: 0,
              fontSize: 38,
              fontWeight: 900,
              color: "#ffffff",
              letterSpacing: 1.5,
              fontFamily: "Arial Black, sans-serif",
            }}
          >
            VOLT REPAIR STUDIO
          </h1>
          <span
            style={{
              fontSize: 20,
              color: "#00f0ff",
              fontWeight: 800,
              letterSpacing: 2,
              textTransform: "uppercase",
              fontFamily: "Arial, sans-serif",
            }}
          >
            Servicio Técnico a Domicilio
          </span>
        </div>
      </div>

      {/* 3. CAJA INFERIOR FLOTANTE CON ACCIÓN DIRECTA (WHATSAPP + GARANTÍA) */}
      <div
        style={{
          position: "absolute",
          bottom: 70,
          left: 45,
          right: 45,
          transform: `scale(${ctaPulse})`,
        }}
      >
        <div
          style={{
            background: "rgba(10, 16, 30, 0.95)",
            border: "3px solid #00f0ff",
            borderRadius: 26,
            padding: "18px 24px",
            textAlign: "center",
            boxShadow: "0 0 35px rgba(0, 240, 255, 0.4)",
            backdropFilter: "blur(14px)",
          }}
        >
          <div
            style={{
              display: "inline-flex",
              alignItems: "center",
              justifyContent: "center",
              gap: 10,
              background: "linear-gradient(135deg, #00f0ff, #0055ff)",
              padding: "12px 26px",
              borderRadius: 16,
              boxShadow: "0 0 20px rgba(0, 240, 255, 0.6)",
              marginBottom: 10,
            }}
          >
            <span
              style={{
                fontSize: 28,
                fontWeight: 900,
                color: "#050914",
                fontFamily: "Arial Black, sans-serif",
              }}
            >
              📲 WhatsApp: 720 815 7790
            </span>
          </div>
          <div
            style={{
              display: "flex",
              justifyContent: "center",
              gap: 18,
              fontSize: 20,
              color: "#e2e8f0",
              fontWeight: 800,
              fontFamily: "Arial, sans-serif",
            }}
          >
            <span>🛡️ 90 Días de Garantía</span>
            <span>•</span>
            <span>📍 En tu sala en 25 min</span>
          </div>
        </div>
      </div>

      {/* 4. BARRA DE PROGRESO INFERIOR DINÁMICA */}
      <div
        style={{
          position: "absolute",
          bottom: 0,
          left: 0,
          height: 14,
          width: `${progressWidth}px`,
          background: "linear-gradient(90deg, #00f0ff, #ff0055, #ffea00)",
          boxShadow: "0 0 20px rgba(0, 240, 255, 0.9)",
        }}
      />

      {/* 5. AUDIO: VOZ HUMANA Y AMISTOSA (ALONSO NEURAL MEXICANO) + BGM TECH DUCKING */}
      <Audio src={staticFile("volt_voice_alonso_short_30s.mp3")} volume={1.0} />
      <Audio src={staticFile("bg_music.webm")} volume={0.12} loop />
    </AbsoluteFill>
  );
};
