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

const SCENES_REEL4: SceneConfig[] = [
  {
    "from": 0,
    "durationInFrames": 119,
    "img": "stock_reel4/scene_01_render-servicio-.jpg",
    "badge": "⚡ VOLT REPAIR STUDIO",
    "headline": "¡QUÉ ONDA AMIGOS!",
    "accent": "#00f0ff"
  },
  {
    "from": 119,
    "durationInFrames": 119,
    "img": "stock_reel4/scene_02_broken_glass_sma.jpg",
    "badge": "💥 TAPA TRASERA ROTA",
    "headline": "¿CRISTAL TRASERO ESTRELLADO?",
    "accent": "#ff0055"
  },
  {
    "from": 238,
    "durationInFrames": 118,
    "img": "stock_reel4/scene_03_heat_gun_repair.jpg",
    "badge": "⚠️ PISTOLA DE CALOR 300°C",
    "headline": "¡PELIGRO CON PISTOLAS DE CALOR!",
    "accent": "#ffea00"
  },
  {
    "from": 356,
    "durationInFrames": 118,
    "img": "stock_reel4/scene_04_camera_sensor_ph.jpg",
    "badge": "📷 SELLOS DERRETIDOS",
    "headline": "EL CALOR ARRUINA TUS CÁMARAS",
    "accent": "#ff0055"
  },
  {
    "from": 474,
    "durationInFrames": 118,
    "img": "stock_reel4/scene_05_swollen_battery.jpg",
    "badge": "🔥 RIESGO EN BATERÍA",
    "headline": "PELIGRO DE CORTO O EXPLOSIÓN",
    "accent": "#ff0055"
  },
  {
    "from": 592,
    "durationInFrames": 118,
    "img": "stock_reel4/scene_06_render-maquina-l.jpg",
    "badge": "⚡ MÁQUINA LÁSER",
    "headline": "TECNOLOGÍA LÁSER DE PRECISIÓN",
    "accent": "#00f0ff"
  },
  {
    "from": 710,
    "durationInFrames": 118,
    "img": "stock_reel4/scene_07_laser_beam_metal.jpg",
    "badge": "🔬 RAYO LÁSER FRÍO",
    "headline": "DESINTEGRA EL PEGAMENTO SIN CALOR",
    "accent": "#a855f7"
  },
  {
    "from": 828,
    "durationInFrames": 118,
    "img": "stock_reel4/scene_08_logic_board_pcb.jpg",
    "badge": "🛡️ CERO CALOR EN PLACA",
    "headline": "CÁMARAS Y CIRCUITOS SEGUROS",
    "accent": "#10b981"
  },
  {
    "from": 946,
    "durationInFrames": 118,
    "img": "stock_reel4/scene_09_precision_pry_to.jpg",
    "badge": "📱 EXTRACCIÓN LIMPIA",
    "headline": "RETIRAMOS CRISTALES SIN RAYONES",
    "accent": "#00f0ff"
  },
  {
    "from": 1064,
    "durationInFrames": 118,
    "img": "stock_reel4/scene_10_new_glass_back_p.jpg",
    "badge": "💎 TAPA NUEVA OEM",
    "headline": "CRISTAL TEMPLADO ORIGINAL",
    "accent": "#10b981"
  },
  {
    "from": 1182,
    "durationInFrames": 118,
    "img": "stock_reel4/scene_11_screen_clamp_rep.jpg",
    "badge": "🔧 PRENSA HERMÉTICA",
    "headline": "SELLADO IMPERMEABLE DE FÁBRICA",
    "accent": "#ffea00"
  },
  {
    "from": 1300,
    "durationInFrames": 118,
    "img": "stock_reel4/scene_12_clean_smartphone.jpg",
    "badge": "✨ RESULTADO IMPECABLE",
    "headline": "TU TELÉFONO COMO NUEVO",
    "accent": "#10b981"
  },
  {
    "from": 1418,
    "durationInFrames": 118,
    "img": "stock_reel4/scene_13_warranty_certifi.jpg",
    "badge": "💵 TARIFA FIJA $500",
    "headline": "SOLO $500 DE MANO DE OBRA",
    "accent": "#10b981"
  },
  {
    "from": 1536,
    "durationInFrames": 118,
    "img": "stock_reel4/scene_14_logo-volt-studio.jpg",
    "badge": "📲 AGENDA HOY MISMO",
    "headline": "¡MÁNDANOS WHATSAPP Y COTIZA YA!",
    "accent": "#00f0ff"
  }
];

const SceneSlide: React.FC<{
  scene: SceneConfig;
  index: number;
}> = ({ scene, index }) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();

  const scale = interpolate(
    frame,
    [0, scene.durationInFrames],
    [1.0, 1.16],
    { extrapolateRight: "clamp" }
  );

  const translateY = interpolate(
    frame,
    [0, scene.durationInFrames],
    index % 2 === 0 ? [-12, 18] : [18, -12],
    { extrapolateRight: "clamp" }
  );

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

export const VoltReel4_Laser: React.FC = () => {
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
      {SCENES_REEL4.map((scene, i) => (
        <Sequence
          key={i}
          from={scene.from}
          durationInFrames={scene.durationInFrames}
        >
          <SceneSlide scene={scene} index={i} />
        </Sequence>
      ))}

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
            boxShadow: "0 0 25px #ff0055aa",
            border: "2px solid #ff0055",
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
              color: "#ff0055",
              fontWeight: 800,
              letterSpacing: 2,
              textTransform: "uppercase",
              fontFamily: "Arial, sans-serif",
            }}
          >
            Láser de Fibra Óptica
          </span>
        </div>
      </div>

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
            border: "3px solid #ff0055",
            borderRadius: 26,
            padding: "18px 24px",
            textAlign: "center",
            boxShadow: "0 0 35px #ff005566",
            backdropFilter: "blur(14px)",
          }}
        >
          <div
            style={{
              display: "inline-flex",
              alignItems: "center",
              justifyContent: "center",
              gap: 10,
              background: "linear-gradient(135deg, #ff0055, #00f0ff)",
              padding: "12px 26px",
              borderRadius: 16,
              boxShadow: "0 0 20px #ff005588",
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

      <div
        style={{
          position: "absolute",
          bottom: 0,
          left: 0,
          height: 14,
          width: `${progressWidth}px`,
          background: "linear-gradient(90deg, #ff0055, #00f0ff, #10b981)",
          boxShadow: "0 0 20px #ff0055cc",
        }}
      />

      <Audio src={staticFile("volt_voice_reel4.mp3")} volume={1.0} />
      <Audio src={staticFile("bg_music.webm")} volume={0.12} loop />
    </AbsoluteFill>
  );
};
