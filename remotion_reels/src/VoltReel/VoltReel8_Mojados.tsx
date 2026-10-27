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

const SCENES_REEL8: SceneConfig[] = [
  {
    "from": 0,
    "durationInFrames": 146,
    "img": "stock_reel8/scene_01_render-servicio-.jpg",
    "badge": "⚡ VOLT REPAIR STUDIO",
    "headline": "¡QUÉ ONDA AMIGOS!",
    "accent": "#00f0ff"
  },
  {
    "from": 146,
    "durationInFrames": 146,
    "img": "stock_reel8/scene_02_phone_in_rice_bo.jpg",
    "badge": "🍚 EL MITO DEL ARROZ",
    "headline": "¡NUNCA METAS TU CEL EN ARROZ!",
    "accent": "#ff0055"
  },
  {
    "from": 292,
    "durationInFrames": 146,
    "img": "stock_reel8/scene_03_damaged_electron.jpg",
    "badge": "❌ PEOR ENEMIGO",
    "headline": "TE VA A COSTAR MILES DE PESOS",
    "accent": "#ffea00"
  },
  {
    "from": 438,
    "durationInFrames": 146,
    "img": "stock_reel8/scene_04_emi_shield_circu.jpg",
    "badge": "⚠️ AGUA ATRAPADA",
    "headline": "EL AGUA SIGUE BAJO LOS BLINDAJES",
    "accent": "#ff0055"
  },
  {
    "from": 584,
    "durationInFrames": 146,
    "img": "stock_reel8/scene_05_green_corrosion_.jpg",
    "badge": "🧪 ALMIDÓN CORROSIVO",
    "headline": "EL ALMIDÓN ACELERA LA CORROSIÓN",
    "accent": "#ff0055"
  },
  {
    "from": 730,
    "durationInFrames": 145,
    "img": "stock_reel8/scene_06_burned_cpu_chip.jpg",
    "badge": "🔥 PISTAS PODRIDAS",
    "headline": "PUDRE PISTAS Y QUEMA EL CHIP",
    "accent": "#ff0055"
  },
  {
    "from": 875,
    "durationInFrames": 145,
    "img": "stock_reel8/scene_07_power_off_phone_.jpg",
    "badge": "⚡ APÁGALO DE INMEDIATO",
    "headline": "¡APÁGALO Y NO LO CONECTES!",
    "accent": "#00f0ff"
  },
  {
    "from": 1020,
    "durationInFrames": 145,
    "img": "stock_reel8/scene_08_mobile_technicia.jpg",
    "badge": "🚗 RESCATE QUÍMICO",
    "headline": "RESCATE QUÍMICO A DOMICILIO",
    "accent": "#00f0ff"
  },
  {
    "from": 1165,
    "durationInFrames": 145,
    "img": "stock_reel8/scene_09_ultrasonic_clean.jpg",
    "badge": "🔬 TINA ULTRASONICA 99%",
    "headline": "TINA ULTRASÓNICA CON ISOPROPÍLICO",
    "accent": "#a855f7"
  },
  {
    "from": 1310,
    "durationInFrames": 145,
    "img": "stock_reel8/scene_10_ultrasonic_cavit.jpg",
    "badge": "✨ ONDAS DE CAVITACIÓN",
    "headline": "ELIMINA SULFATO Y MINERALES",
    "accent": "#10b981"
  },
  {
    "from": 1455,
    "durationInFrames": 145,
    "img": "stock_reel8/scene_11_multimeter_test_.jpg",
    "badge": "🔧 SECADO Y MULTÍMETRO",
    "headline": "SECADO CONTROLADO Y CERO CORTOS",
    "accent": "#ffea00"
  },
  {
    "from": 1600,
    "durationInFrames": 145,
    "img": "stock_reel8/scene_12_happy_client_wor.jpg",
    "badge": "💎 SALVAMOS TUS FOTOS",
    "headline": "SALVAMOS TUS DATOS POR $500",
    "accent": "#10b981"
  },
  {
    "from": 1745,
    "durationInFrames": 145,
    "img": "stock_reel8/scene_13_logo-volt-studio.jpg",
    "badge": "📲 AGENDA HOY MISMO",
    "headline": "¡MÁNDANOS WHATSAPP DE VOLADA!",
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

export const VoltReel8_Mojados: React.FC = () => {
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
      {SCENES_REEL8.map((scene, i) => (
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
            boxShadow: "0 0 25px #10b981aa",
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
            Desoxidación Ultrasónica 99%
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
            border: "3px solid #10b981",
            borderRadius: 26,
            padding: "18px 24px",
            textAlign: "center",
            boxShadow: "0 0 35px #10b98166",
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
              boxShadow: "0 0 20px #10b98188",
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
          background: "linear-gradient(90deg, #10b981, #00f0ff, #10b981)",
          boxShadow: "0 0 20px #10b981cc",
        }}
      />

      <Audio src={staticFile("volt_voice_reel8.mp3")} volume={1.0} />
      <Audio src={staticFile("bg_music.webm")} volume={0.12} loop />
    </AbsoluteFill>
  );
};
