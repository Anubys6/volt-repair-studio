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
  img: string;
  badge: string;
  headline: string;
  accent: string;
}

const SCENES: SceneConfig[] = [
  {
    img: "stock/scene_01_broken.jpg",
    badge: "⚠️ DIAGNÓSTICO EN TU SALA",
    headline: "¿POR QUÉ LE TIENEN TANTO MIEDO A LOS TALLERES?",
    accent: "#ff0055",
  },
  {
    img: "stock/scene_02_screws.jpg",
    badge: "🔧 TORNILLOS PENTALOBE",
    headline: "DESMONTAJE DE PRECISIÓN FRENTE A TI",
    accent: "#00f0ff",
  },
  {
    img: "stock/scene_03_lift.jpg",
    badge: "📱 APERTURA CON VENTOSA",
    headline: "CERO RAYONES EN EL CHASIS DE TU EQUIPO",
    accent: "#00f0ff",
  },
  {
    img: "stock/scene_04_shields.jpg",
    badge: "👀 TRANSPARENCIA TOTAL",
    headline: "DESCONEXIÓN DE BLINDAJES ANTE TUS OJOS",
    accent: "#ffea00",
  },
  {
    img: "stock/scene_05_board.jpg",
    badge: "🔬 MICROELECTRÓNICA",
    headline: "CALIBRACIÓN DE SENSORES Y MICROCHIPS",
    accent: "#a855f7",
  },
  {
    img: "stock/scene_06_connectors.jpg",
    badge: "🛡️ REFACCIONES GRADO A+",
    headline: "CONEXIONES LIMPIAS Y PROTECCIÓN TÉRMICA",
    accent: "#00f0ff",
  },
  {
    img: "stock/scene_07_new_screen.jpg",
    badge: "⚡ MANO DE OBRA FIJA $700",
    headline: "INSTALACIÓN DE NUEVA PANTALLA EN 25 MIN",
    accent: "#10b981",
  },
  {
    img: "stock/scene_08_tested.jpg",
    badge: "✨ TRUE TONE CONSERVADO",
    headline: "PRUEBAS TÁCTILES Y COLORES ORIGINALES",
    accent: "#ffea00",
  },
  {
    img: "stock/scene_09_pristine.jpg",
    badge: "💎 RESULTADO IMPECABLE",
    headline: "TU CELULAR COMO NUEVO SIN BORRAR TUS FOTOS",
    accent: "#10b981",
  },
  {
    img: "stock/scene_10_workbench.jpg",
    badge: "📲 AGENDA HOY MISMO",
    headline: "MÁNDANOS WHATSAPP Y TE COTIZAMOS DE VOLADA",
    accent: "#00f0ff",
  },
];

const SCENE_DURATION_FRAMES = 93; // 93 fotogramas * 10 escenas = 930 frames (31 segundos a 30fps)

// Componente individual de cada escena con movimiento continuo Ken Burns
const SceneSlide: React.FC<{
  scene: SceneConfig;
  index: number;
}> = ({ scene, index }) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();

  // Movimiento continuo: zoom del 100% al 118% durante toda la escena (nunca estático)
  const scale = interpolate(
    frame,
    [0, SCENE_DURATION_FRAMES],
    [1.0, 1.18],
    { extrapolateRight: "clamp" }
  );

  // Desplazamiento sutil hacia arriba o hacia los lados para dar dinamismo cinematográfico
  const translateY = interpolate(
    frame,
    [0, SCENE_DURATION_FRAMES],
    index % 2 === 0 ? [-10, 20] : [20, -10],
    { extrapolateRight: "clamp" }
  );

  // Transición suave de entrada (crossfade)
  const fadeIn = interpolate(frame, [0, 8], [0, 1], {
    extrapolateRight: "clamp",
  });

  // Animación del texto con resorte físico
  const textSpring = spring({
    frame,
    fps,
    config: { damping: 140, mass: 0.6 },
  });

  return (
    <AbsoluteFill style={{ opacity: fadeIn }}>
      {/* Fotografía técnica con movimiento continuo */}
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

      {/* Viñeta cinematográfica oscura (degradado para que los textos resalten al 100%) */}
      <AbsoluteFill
        style={{
          background:
            "linear-gradient(180deg, rgba(6, 9, 17, 0.90) 0%, rgba(6, 9, 17, 0.20) 25%, rgba(6, 9, 17, 0.25) 60%, rgba(6, 9, 17, 0.96) 100%)",
        }}
      />

      {/* Badge de la etapa en movimiento */}
      <div
        style={{
          position: "absolute",
          top: 180,
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
            boxShadow: `0 0 30px ${scene.accent}88`,
          }}
        >
          {scene.badge}
        </div>
      </div>

      {/* Titular cinemático de alto impacto (zona segura vertical) */}
      <div
        style={{
          position: "absolute",
          top: 270,
          left: 50,
          right: 50,
          textAlign: "center",
          transform: `translateY(${interpolate(textSpring, [0, 1], [30, 0])}px)`,
        }}
      >
        <h2
          style={{
            fontSize: 52,
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
      {/* 1. SECUENCIA DINÁMICA DE 10 FOTOS TÉCNICAS (CAMBIO CONSTANTE Y MOVIMIENTO KEN BURNS) */}
      {SCENES.map((scene, i) => (
        <Sequence
          key={i}
          from={i * SCENE_DURATION_FRAMES}
          durationInFrames={SCENE_DURATION_FRAMES}
        >
          <SceneSlide scene={scene} index={i} />
        </Sequence>
      ))}

      {/* 2. HEADER PERMANENTE CON BRANDING OFICIAL */}
      <div
        style={{
          position: "absolute",
          top: 60,
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
            padding: "20px 28px",
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
              padding: "12px 28px",
              borderRadius: 16,
              boxShadow: "0 0 20px rgba(0, 240, 255, 0.6)",
              marginBottom: 10,
            }}
          >
            <span
              style={{
                fontSize: 30,
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
              gap: 20,
              fontSize: 21,
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

      {/* 5. AUDIO: LOCUCIÓN PROFESIONAL + MÚSICA LO-FI TECH CON DUCKING */}
      <Audio src={staticFile("volt_voice_1.mp3")} volume={1.0} />
      <Audio src={staticFile("bg_music.webm")} volume={0.14} loop />
    </AbsoluteFill>
  );
};
