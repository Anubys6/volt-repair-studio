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

const SCENES_REEL2: SceneConfig[] = [
  {
    from: 0,
    durationInFrames: 54, // 0.0s - 1.80s
    img: "stock_reel2/scene_01_intro.jpg",
    badge: "⚡ VOLT REPAIR STUDIO",
    headline: "¡QUÉ ONDA AMIGOS!",
    accent: "#00f0ff",
  },
  {
    from: 54,
    durationInFrames: 70, // 1.80s - 4.13s
    img: "stock_reel2/scene_02a_truetone_lost.jpg",
    badge: "⚠️ TRUE TONE DESAPARECIDO",
    headline: "¿PERDISTE EL TRUE TONE?",
    accent: "#ff0055",
  },
  {
    from: 124,
    durationInFrames: 70, // 4.13s - 6.47s
    img: "stock_reel2/scene_02b_bad_shop.jpg",
    badge: "❌ TALLERES CALLEJEROS",
    headline: "PANTALLAS SIN CALIBRACIÓN",
    accent: "#ffea00",
  },
  {
    from: 194,
    durationInFrames: 94, // 6.47s - 9.60s
    img: "stock_reel2/scene_03_sensor_glitch.jpg",
    badge: "📉 SENSOR DESCALIBRADO",
    headline: "BRILLO AUTOMÁTICO DESACTIVADO",
    accent: "#ff0055",
  },
  {
    from: 288,
    durationInFrames: 77, // 9.60s - 12.17s
    img: "stock_reel2/scene_04a_eeprom_chip.jpg",
    badge: "🔬 SERIALES CRIPTOGRÁFICOS",
    headline: "CHIP EEPROM SIN TRANSFERIR",
    accent: "#a855f7",
  },
  {
    from: 365,
    durationInFrames: 77, // 12.17s - 14.73s
    img: "stock_reel2/scene_04b_display_serial.jpg",
    badge: "📱 SERIAL ORIGINAL PERDIDO",
    headline: "NO COPIAN EL MICROCHIP",
    accent: "#ffea00",
  },
  {
    from: 442,
    durationInFrames: 112, // 14.73s - 18.47s
    img: "stock_reel2/scene_05_lab_level.jpg",
    badge: "💎 NIVEL DE LABORATORIO",
    headline: "INGENIERÍA Y CALIBRACIÓN REAL",
    accent: "#00f0ff",
  },
  {
    from: 554,
    durationInFrames: 103, // 18.47s - 21.90s
    img: "stock_reel2/scene_06_jcid_tool.jpg",
    badge: "🔬 PROGRAMADORA JCID",
    headline: "LLEVAMOS LA PROGRAMADORA A TU CASA",
    accent: "#a855f7",
  },
  {
    from: 657,
    durationInFrames: 75, // 21.90s - 24.40s
    img: "stock_reel2/scene_07a_connect_old.jpg",
    badge: "⚡ LECTURA DE CHIP",
    headline: "CONECTAMOS TU PANTALLA ROTA",
    accent: "#00f0ff",
  },
  {
    from: 732,
    durationInFrames: 76, // 24.40s - 26.93s
    img: "stock_reel2/scene_07b_extract_serial.jpg",
    badge: "🔑 SERIAL DE FÁBRICA",
    headline: "EXTRAEMOS EL CÓDIGO CRIPTOGRÁFICO",
    accent: "#ffea00",
  },
  {
    from: 808,
    durationInFrames: 132, // 26.93s - 31.33s
    img: "stock_reel2/scene_08_write_new.jpg",
    badge: "🛡️ REFACCIÓN CERTIFICADA",
    headline: "TRANSFERIMOS A PANTALLA GRADO A+",
    accent: "#10b981",
  },
  {
    from: 940,
    durationInFrames: 150, // 31.33s - 36.33s
    img: "stock_reel2/scene_09_vivid_120hz.jpg",
    badge: "✨ 120 HZ Y TRUE TONE",
    headline: "COLORES Y FLUIDEZ DE FÁBRICA",
    accent: "#00f0ff",
  },
  {
    from: 1090,
    durationInFrames: 137, // 36.33s - 40.90s
    img: "stock_reel2/scene_10_live_dining.jpg",
    badge: "🏠 PRUEBAS EN TU COMEDOR",
    headline: "CALIBRACIÓN EN VIVO EN 25 MIN",
    accent: "#10b981",
  },
  {
    from: 1227,
    durationInFrames: 82, // 40.90s - 43.63s
    img: "stock_reel2/scene_11a_price700.jpg",
    badge: "💵 TARIFA FIJA",
    headline: "MANO DE OBRA FIJA DE SOLO $700",
    accent: "#10b981",
  },
  {
    from: 1309,
    durationInFrames: 82, // 43.63s - 46.37s
    img: "stock_reel2/scene_11b_warranty.jpg",
    badge: "🛡️ 90 DÍAS DE GARANTÍA",
    headline: "RESPALDO TOTAL POR ESCRITO",
    accent: "#ffea00",
  },
  {
    from: 1391,
    durationInFrames: 110, // 46.37s - 50.04s
    img: "stock_reel2/scene_12_whatsapp.jpg",
    badge: "📲 AGENDA HOY MISMO",
    headline: "¡MÁNDANOS WHATSAPP Y COTIZA YA!",
    accent: "#00f0ff",
  },
];

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

  // Transición suave de entrada (crossfade)
  const fadeIn = interpolate(frame, [0, 5], [0, 1], {
    extrapolateRight: "clamp",
  });

  const textSpring = spring({
    frame,
    fps,
    config: { damping: 140, mass: 0.55 },
  });

  return (
    <AbsoluteFill style={{ opacity: fadeIn }}>
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

export const VoltReel2_TrueTone: React.FC = () => {
  const frame = useCurrentFrame();
  const { fps, durationInFrames, width } = useVideoConfig();

  const headerEntrance = spring({
    frame,
    fps,
    config: { damping: 200, mass: 0.5 },
  });

  const ctaPulse = interpolate(
    Math.sin((frame / fps) * 3.5),
    [-1, 1],
    [0.985, 1.015]
  );

  const progressWidth = interpolate(frame, [0, durationInFrames], [0, width], {
    extrapolateRight: "clamp",
  });

  return (
    <AbsoluteFill style={{ backgroundColor: "#060911" }}>
      {/* SECUENCIA DINÁMICA DE 16 FOTOS TÉCNICAS CONGRUENTES */}
      {SCENES_REEL2.map((scene, i) => (
        <Sequence
          key={i}
          from={scene.from}
          durationInFrames={scene.durationInFrames}
        >
          <SceneSlide scene={scene} index={i} />
        </Sequence>
      ))}

      {/* HEADER PERMANENTE CON BRANDING OFICIAL */}
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
              color: "#a855f7",
              fontWeight: 800,
              letterSpacing: 2,
              textTransform: "uppercase",
              fontFamily: "Arial, sans-serif",
            }}
          >
            Programación EEPROM True Tone
          </span>
        </div>
      </div>

      {/* CAJA INFERIOR FLOTANTE CON ACCIÓN DIRECTA (WHATSAPP + GARANTÍA) */}
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
            border: "3px solid #a855f7",
            borderRadius: 26,
            padding: "18px 24px",
            textAlign: "center",
            boxShadow: "0 0 35px rgba(168, 85, 247, 0.4)",
            backdropFilter: "blur(14px)",
          }}
        >
          <div
            style={{
              display: "inline-flex",
              alignItems: "center",
              justifyContent: "center",
              gap: 10,
              background: "linear-gradient(135deg, #a855f7, #00f0ff)",
              padding: "12px 26px",
              borderRadius: 16,
              boxShadow: "0 0 20px rgba(168, 85, 247, 0.6)",
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

      {/* BARRA DE PROGRESO INFERIOR DINÁMICA */}
      <div
        style={{
          position: "absolute",
          bottom: 0,
          left: 0,
          height: 14,
          width: `${progressWidth}px`,
          background: "linear-gradient(90deg, #a855f7, #00f0ff, #10b981)",
          boxShadow: "0 0 20px rgba(168, 85, 247, 0.9)",
        }}
      />

      {/* AUDIO: VOZ HUMANA AMISTOSA (ALONSO NEURAL) + BGM TECH DUCKING */}
      <Audio src={staticFile("volt_voice_reel2_truetone.mp3")} volume={1.0} />
      <Audio src={staticFile("bg_music.webm")} volume={0.12} loop />
    </AbsoluteFill>
  );
};
