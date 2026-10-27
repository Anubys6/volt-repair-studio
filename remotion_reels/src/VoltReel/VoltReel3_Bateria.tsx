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

const SCENES_REEL3: SceneConfig[] = [
  {
    from: 0,
    durationInFrames: 54, // 0.0s - 1.80s
    img: "stock_reel3/scene_01_intro.jpg",
    badge: "⚡ VOLT REPAIR STUDIO",
    headline: "¡QUÉ ONDA AMIGOS!",
    accent: "#00f0ff",
  },
  {
    from: 54,
    durationInFrames: 63, // 1.80s - 3.90s
    img: "stock_reel3/scene_02a_street_danger.jpg",
    badge: "⚠️ ALERTA EN BATERÍAS",
    headline: "¡CUIDADO CON TALLERES DE CALLE!",
    accent: "#ff0055",
  },
  {
    from: 117,
    durationInFrames: 63, // 3.90s - 6.00s
    img: "stock_reel3/scene_02b_bad_kiosk.jpg",
    badge: "❌ MALAS PRÁCTICAS",
    headline: "PEGAMENTOS QUE DEFORMAN CELDAS",
    accent: "#ffea00",
  },
  {
    from: 180,
    durationInFrames: 61, // 6.00s - 8.03s
    img: "stock_reel3/scene_03a_draining.jpg",
    badge: "🔋 BATERÍA DEGRADADA",
    headline: "¿SE DESCARGA EN POCAS HORAS?",
    accent: "#ff0055",
  },
  {
    from: 241,
    durationInFrames: 61, // 8.03s - 10.07s
    img: "stock_reel3/scene_03b_overheating.jpg",
    badge: "🔥 SOBRECALENTAMIENTO",
    headline: "¿SE CALIENTA TU CELULAR?",
    accent: "#ff0055",
  },
  {
    from: 302,
    durationInFrames: 79, // 10.07s - 12.70s
    img: "stock_reel3/scene_04a_school_tape.jpg",
    badge: "❌ CINTA ESCOLAR DOBLE CARA",
    headline: "PEGAN BATERÍAS CON RESISTOL",
    accent: "#ffea00",
  },
  {
    from: 381,
    durationInFrames: 80, // 12.70s - 15.37s
    img: "stock_reel3/scene_04b_scraped_glue.jpg",
    badge: "⚠️ PELIGRO DE CORTO",
    headline: "PEGAMENTO QUE DAÑA EL CHASIS",
    accent: "#ff0055",
  },
  {
    from: 461,
    durationInFrames: 142, // 15.37s - 20.10s
    img: "stock_reel3/scene_05_deformed_cell.jpg",
    badge: "🔥 RIESGO TÉRMICO",
    headline: "DEFORMAN LA CELDA Y EL PROCESADOR",
    accent: "#ff0055",
  },
  {
    from: 603,
    durationInFrames: 111, // 20.10s - 23.80s
    img: "stock_reel3/scene_06_factory_standard.jpg",
    badge: "💎 ESTÁNDAR DE FÁBRICA",
    headline: "CALIDAD Y SEGURIDAD CERTIFICADA",
    accent: "#10b981",
  },
  {
    from: 714,
    durationInFrames: 153, // 23.80s - 28.90s
    img: "stock_reel3/scene_07_dining_repair.jpg",
    badge: "🏠 SERVICIO EN TU COMEDOR",
    headline: "EN TU CASA EN 20 MINUTOS",
    accent: "#00f0ff",
  },
  {
    from: 867,
    durationInFrames: 152, // 28.90s - 33.97s
    img: "stock_reel3/scene_08_safe_disconnect.jpg",
    badge: "🔧 EXTRACCIÓN DE PRECISIÓN",
    headline: "CERO PRESIÓN EN CIRCUITOS",
    accent: "#00f0ff",
  },
  {
    from: 1019,
    durationInFrames: 87, // 33.97s - 36.87s
    img: "stock_reel3/scene_09a_pulltabs.jpg",
    badge: "🛡️ TIRAS ELÁSTICAS PULL-TABS",
    headline: "ADHESIVO TÉRMICO DE FÁBRICA",
    accent: "#10b981",
  },
  {
    from: 1106,
    durationInFrames: 87, // 36.87s - 39.77s
    img: "stock_reel3/scene_09b_new_cell.jpg",
    badge: "⚡ CELDA DE ALTA DENSIDAD",
    headline: "BATERÍA CERTIFICADA OEM",
    accent: "#00f0ff",
  },
  {
    from: 1193,
    durationInFrames: 136, // 39.77s - 44.30s
    img: "stock_reel3/scene_10_health100.jpg",
    badge: "✨ CONDICIÓN AL 100%",
    headline: "DISIPA CALOR Y MÁXIMA DURACIÓN",
    accent: "#10b981",
  },
  {
    from: 1329,
    durationInFrames: 86, // 44.30s - 47.17s
    img: "stock_reel3/scene_11a_price500.jpg",
    badge: "💵 MANO DE OBRA FIJA $500",
    headline: "TARIFA FIJA SIN SORPRESAS",
    accent: "#10b981",
  },
  {
    from: 1415,
    durationInFrames: 86, // 47.17s - 50.03s
    img: "stock_reel3/scene_11b_warranty.jpg",
    badge: "🛡️ 90 DÍAS DE GARANTÍA",
    headline: "GARANTÍA TOTAL POR ESCRITO",
    accent: "#ffea00",
  },
  {
    from: 1501,
    durationInFrames: 122, // 50.03s - 54.10s
    img: "stock_reel3/scene_12_whatsapp.jpg",
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

export const VoltReel3_Bateria: React.FC = () => {
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
      {/* SECUENCIA DINÁMICA DE 17 FOTOS TÉCNICAS CONGRUENTES */}
      {SCENES_REEL3.map((scene, i) => (
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
            boxShadow: "0 0 25px rgba(16, 185, 129, 0.7)",
            border: "2px solid #10b981",
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
              color: "#10b981",
              fontWeight: 800,
              letterSpacing: 2,
              textTransform: "uppercase",
              fontFamily: "Arial, sans-serif",
            }}
          >
            Batería Certificada Pull-Tabs OEM
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
            border: "3px solid #10b981",
            borderRadius: 26,
            padding: "18px 24px",
            textAlign: "center",
            boxShadow: "0 0 35px rgba(16, 185, 129, 0.4)",
            backdropFilter: "blur(14px)",
          }}
        >
          <div
            style={{
              display: "inline-flex",
              alignItems: "center",
              justifyContent: "center",
              gap: 10,
              background: "linear-gradient(135deg, #10b981, #00f0ff)",
              padding: "12px 26px",
              borderRadius: 16,
              boxShadow: "0 0 20px rgba(16, 185, 129, 0.6)",
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
            <span>📍 En tu sala en 20 min</span>
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
          background: "linear-gradient(90deg, #10b981, #00f0ff, #ffea00)",
          boxShadow: "0 0 20px rgba(16, 185, 129, 0.9)",
        }}
      />

      {/* AUDIO: VOZ HUMANA AMISTOSA (ALONSO NEURAL) + BGM TECH DUCKING */}
      <Audio src={staticFile("volt_voice_reel3_bateria.mp3")} volume={1.0} />
      <Audio src={staticFile("bg_music.webm")} volume={0.12} loop />
    </AbsoluteFill>
  );
};
