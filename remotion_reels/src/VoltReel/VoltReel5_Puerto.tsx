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

const SCENES_REEL5: SceneConfig[] = [
  {
    "from": 0,
    "durationInFrames": 135,
    "img": "stock_reel5/scene_01_render-servicio-.jpg",
    "badge": "⚡ VOLT REPAIR STUDIO",
    "headline": "¡QUÉ ONDA AMIGOS!",
    "accent": "#00f0ff"
  },
  {
    "from": 135,
    "durationInFrames": 135,
    "img": "stock_reel5/scene_02_usb_c_cable_phon.jpg",
    "badge": "🔌 NO AGARRA CARGA",
    "headline": "¿BATALLAS PARA QUE CARGUE?",
    "accent": "#ff0055"
  },
  {
    "from": 270,
    "durationInFrames": 135,
    "img": "stock_reel5/scene_03_repair_shop_scam.jpg",
    "badge": "❌ ESTAFAS EN CALLE",
    "headline": "NO PAGUES $800 POR CAMBIO DE PUERTO",
    "accent": "#ffea00"
  },
  {
    "from": 405,
    "durationInFrames": 135,
    "img": "stock_reel5/scene_04_usb_c_port_macro.jpg",
    "badge": "📱 PUERTO EN BUEN ESTADO",
    "headline": "¡TU CENTRO DE CARGA ESTÁ SANO!",
    "accent": "#10b981"
  },
  {
    "from": 540,
    "durationInFrames": 134,
    "img": "stock_reel5/scene_05_pocket_lint_clos.jpg",
    "badge": "⚠️ PELUSA COMPACTADA",
    "headline": "PELUSA DE BOLSILLO AL FONDO",
    "accent": "#ff0055"
  },
  {
    "from": 674,
    "durationInFrames": 134,
    "img": "stock_reel5/scene_06_usb_c_connector_.jpg",
    "badge": "📉 FALSO CONTACTO",
    "headline": "EL CONECTOR CHOCA CON LA PELUSA",
    "accent": "#ffea00"
  },
  {
    "from": 808,
    "durationInFrames": 134,
    "img": "stock_reel5/scene_07_living_room_desk.jpg",
    "badge": "🏠 SERVICIO EN TU COMEDOR",
    "headline": "REVISIÓN EN TU SALA EN 15 MIN",
    "accent": "#00f0ff"
  },
  {
    "from": 942,
    "durationInFrames": 134,
    "img": "stock_reel5/scene_08_stereo_microscop.jpg",
    "badge": "🔬 MICROSCOPIO ÓPTICO",
    "headline": "INSTRUMENTAL ANTIESTÁTICO FINO",
    "accent": "#a855f7"
  },
  {
    "from": 1076,
    "durationInFrames": 134,
    "img": "stock_reel5/scene_09_copper_contact_p.jpg",
    "badge": "✨ LIMPIEZA PROFUNDA",
    "headline": "EXTRACCIÓN SIN DOBLAR PINES",
    "accent": "#10b981"
  },
  {
    "from": 1210,
    "durationInFrames": 134,
    "img": "stock_reel5/scene_10_usb_tester_meter.jpg",
    "badge": "⚡ TESTER USB DIGITAL",
    "headline": "MEDICIÓN DE VOLTAJE Y AMPERAJE",
    "accent": "#00f0ff"
  },
  {
    "from": 1344,
    "durationInFrames": 134,
    "img": "stock_reel5/scene_11_honest_repair_se.jpg",
    "badge": "💎 HONESTIDAD TOTAL",
    "headline": "SOLO COBRAMOS LIMPIEZA BÁSICA",
    "accent": "#10b981"
  },
  {
    "from": 1478,
    "durationInFrames": 134,
    "img": "stock_reel5/scene_12_fast_charging_in.jpg",
    "badge": "🛡️ RESPALDO ESCRITO",
    "headline": "GARANTÍA DE 90 DÍAS POR ESCRITO",
    "accent": "#ffea00"
  },
  {
    "from": 1612,
    "durationInFrames": 134,
    "img": "stock_reel5/scene_13_logo-volt-studio.jpg",
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

export const VoltReel5_Puerto: React.FC = () => {
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
      {SCENES_REEL5.map((scene, i) => (
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
            boxShadow: "0 0 25px #00f0ffaa",
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
            Limpieza Antiestática de Puerto
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
            border: "3px solid #00f0ff",
            borderRadius: 26,
            padding: "18px 24px",
            textAlign: "center",
            boxShadow: "0 0 35px #00f0ff66",
            backdropFilter: "blur(14px)",
          }}
        >
          <div
            style={{
              display: "inline-flex",
              alignItems: "center",
              justifyContent: "center",
              gap: 10,
              background: "linear-gradient(135deg, #00f0ff, #00f0ff)",
              padding: "12px 26px",
              borderRadius: 16,
              boxShadow: "0 0 20px #00f0ff88",
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
          background: "linear-gradient(90deg, #00f0ff, #00f0ff, #10b981)",
          boxShadow: "0 0 20px #00f0ffcc",
        }}
      />

      <Audio src={staticFile("volt_voice_reel5.mp3")} volume={1.0} />
      <Audio src={staticFile("bg_music.webm")} volume={0.12} loop />
    </AbsoluteFill>
  );
};
