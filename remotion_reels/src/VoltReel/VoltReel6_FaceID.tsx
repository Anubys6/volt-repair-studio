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

const SCENES_REEL6: SceneConfig[] = [
  {
    "from": 0,
    "durationInFrames": 134,
    "img": "stock_reel6/scene_01_render-servicio-.jpg",
    "badge": "⚡ VOLT REPAIR STUDIO",
    "headline": "¡QUÉ ONDA AMIGOS!",
    "accent": "#00f0ff"
  },
  {
    "from": 134,
    "durationInFrames": 134,
    "img": "stock_reel6/scene_02_face_id_not_work.jpg",
    "badge": "🔒 FACE ID DESACTIVADO",
    "headline": "¿TE DIJERON QUE YA NO SIRVE?",
    "accent": "#ff0055"
  },
  {
    "from": 268,
    "durationInFrames": 134,
    "img": "stock_reel6/scene_03_bad_soldering_pc.jpg",
    "badge": "❌ FALTA DE TÉCNICA",
    "headline": "NO SABEN DE MICROELECTRÓNICA",
    "accent": "#ffea00"
  },
  {
    "from": 402,
    "durationInFrames": 134,
    "img": "stock_reel6/scene_04_torn_flex_ribbon.jpg",
    "badge": "⚠️ FLEXOR RASGADO",
    "headline": "ROMPEN EL SENSOR DOT PROJECTOR",
    "accent": "#ff0055"
  },
  {
    "from": 536,
    "durationInFrames": 134,
    "img": "stock_reel6/scene_05_infrared_dot_pro.jpg",
    "badge": "🔬 30,000 PUNTOS LÁSER",
    "headline": "EMITE 30,000 PUNTOS INFRARROJOS",
    "accent": "#a855f7"
  },
  {
    "from": 670,
    "durationInFrames": 134,
    "img": "stock_reel6/scene_06_security_lock_ch.jpg",
    "badge": "🛡️ BLOQUEO BIOMÉTRICO",
    "headline": "BLOQUEO DE SEGURIDAD BIOMÉTRICA",
    "accent": "#ff0055"
  },
  {
    "from": 804,
    "durationInFrames": 134,
    "img": "stock_reel6/scene_07_render-equipo-mi.jpg",
    "badge": "💎 MICRO-CIRUGÍA",
    "headline": "REPARACIÓN BAJO MICROSCOPIO",
    "accent": "#00f0ff"
  },
  {
    "from": 938,
    "durationInFrames": 134,
    "img": "stock_reel6/scene_08_fine_tip_solderi.jpg",
    "badge": "🔧 CAUTÍN DE ALTA FRECUENCIA",
    "headline": "EXTRACCIÓN TÉRMICA DE PRECISIÓN",
    "accent": "#ffea00"
  },
  {
    "from": 1072,
    "durationInFrames": 134,
    "img": "stock_reel6/scene_09_jumper_wire_micr.jpg",
    "badge": "🔬 MICRO-JUMPERS DE PLATA",
    "headline": "PUENTES MÁS DELGADOS QUE UN CABELLO",
    "accent": "#a855f7"
  },
  {
    "from": 1206,
    "durationInFrames": 134,
    "img": "stock_reel6/scene_10_jcid_face_id_tag.jpg",
    "badge": "⚡ TRASPLANTE DE CHIP",
    "headline": "NUEVO FLEXOR PROGRAMABLE JCID",
    "accent": "#00f0ff"
  },
  {
    "from": 1340,
    "durationInFrames": 134,
    "img": "stock_reel6/scene_11_infrared_camera_.jpg",
    "badge": "✨ PRUEBA INFRARROJA",
    "headline": "TEST DE HAZ INFRARROJO EN VIVO",
    "accent": "#10b981"
  },
  {
    "from": 1474,
    "durationInFrames": 134,
    "img": "stock_reel6/scene_12_face_unlock_smil.jpg",
    "badge": "📱 DESBLOQUEO AL INSTANTE",
    "headline": "FACE ID RECUPERADO AL 100%",
    "accent": "#10b981"
  },
  {
    "from": 1608,
    "durationInFrames": 133,
    "img": "stock_reel6/scene_13_warranty_certifi.jpg",
    "badge": "💵 MANO DE OBRA FIJA $700",
    "headline": "90 DÍAS DE GARANTÍA POR ESCRITO",
    "accent": "#ffea00"
  },
  {
    "from": 1741,
    "durationInFrames": 133,
    "img": "stock_reel6/scene_14_logo-volt-studio.jpg",
    "badge": "📲 AGENDA HOY MISMO",
    "headline": "¡RECUPERA TU FACE ID DE VOLADA!",
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

export const VoltReel6_FaceID: React.FC = () => {
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
      {SCENES_REEL6.map((scene, i) => (
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
            boxShadow: "0 0 25px #a855f7aa",
            border: "2px solid #a855f7",
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
            Microelectrónica Dot Projector
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
            border: "3px solid #a855f7",
            borderRadius: 26,
            padding: "18px 24px",
            textAlign: "center",
            boxShadow: "0 0 35px #a855f766",
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
              boxShadow: "0 0 20px #a855f788",
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
          background: "linear-gradient(90deg, #a855f7, #00f0ff, #10b981)",
          boxShadow: "0 0 20px #a855f7cc",
        }}
      />

      <Audio src={staticFile("volt_voice_reel6.mp3")} volume={1.0} />
      <Audio src={staticFile("bg_music.webm")} volume={0.12} loop />
    </AbsoluteFill>
  );
};
