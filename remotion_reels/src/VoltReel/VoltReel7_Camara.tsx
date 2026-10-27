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

const SCENES_REEL7: SceneConfig[] = [
  {
    "from": 0,
    "durationInFrames": 139,
    "img": "stock_reel7/scene_01_render-servicio-.jpg",
    "badge": "⚡ VOLT REPAIR STUDIO",
    "headline": "¡QUÉ ONDA AMIGOS!",
    "accent": "#00f0ff"
  },
  {
    "from": 139,
    "durationInFrames": 139,
    "img": "stock_reel7/scene_02_blurry_camera_ph.jpg",
    "badge": "📷 CÁMARA TEMBLOROSA",
    "headline": "¿LA CÁMARA TIEMBLA Y ZUMBA?",
    "accent": "#ff0055"
  },
  {
    "from": 278,
    "durationInFrames": 139,
    "img": "stock_reel7/scene_03_motorcycle_phone.jpg",
    "badge": "🏍️ VIBRACIÓN DE MOTO",
    "headline": "CULPA DEL SOPORTE DE LA MOTO",
    "accent": "#ffea00"
  },
  {
    "from": 417,
    "durationInFrames": 139,
    "img": "stock_reel7/scene_04_ois_optical_imag.jpg",
    "badge": "⚠️ ELECTROIMANES ROTOS",
    "headline": "SE ROMPE EL ESTABILIZADOR OIS",
    "accent": "#ff0055"
  },
  {
    "from": 556,
    "durationInFrames": 139,
    "img": "stock_reel7/scene_05_unknown_part_war.jpg",
    "badge": "❌ CÁMARAS USADAS",
    "headline": "BOTAN ALERTA DE PIEZA DESCONOCIDA",
    "accent": "#ff0055"
  },
  {
    "from": 695,
    "durationInFrames": 139,
    "img": "stock_reel7/scene_06_living_room_tabl.jpg",
    "badge": "🏠 EN TU PROPIA SALA",
    "headline": "EN TU CASA EN 25 MINUTOS",
    "accent": "#00f0ff"
  },
  {
    "from": 834,
    "durationInFrames": 139,
    "img": "stock_reel7/scene_07_camera_module_di.jpg",
    "badge": "🔧 DESMONTAJE SEGURO",
    "headline": "RETIRAMOS EL MÓDULO DAÑADO",
    "accent": "#00f0ff"
  },
  {
    "from": 973,
    "durationInFrames": 138,
    "img": "stock_reel7/scene_08_sapphire_camera_.jpg",
    "badge": "💎 CRISTAL DE ZAFIRO OEM",
    "headline": "CÁMARA CERTIFICADA DE FÁBRICA",
    "accent": "#10b981"
  },
  {
    "from": 1111,
    "durationInFrames": 138,
    "img": "stock_reel7/scene_09_macro_focus_test.jpg",
    "badge": "🔬 CALIBRACIÓN EN VIVO",
    "headline": "TEST DE MACRO Y ZOOM EN VIVO",
    "accent": "#a855f7"
  },
  {
    "from": 1249,
    "durationInFrames": 138,
    "img": "stock_reel7/scene_10_smooth_cinematic.jpg",
    "badge": "✨ VIDEO 4K ULTRA FLUIDO",
    "headline": "VIDEOS ULTRA ESTABLES EN 4K",
    "accent": "#10b981"
  },
  {
    "from": 1387,
    "durationInFrames": 138,
    "img": "stock_reel7/scene_11_warranty_certifi.jpg",
    "badge": "💵 MANO DE OBRA FIJA $600",
    "headline": "SOLO $600 CON 90 DÍAS GARANTÍA",
    "accent": "#ffea00"
  },
  {
    "from": 1525,
    "durationInFrames": 138,
    "img": "stock_reel7/scene_12_logo-volt-studio.jpg",
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

export const VoltReel7_Camara: React.FC = () => {
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
      {SCENES_REEL7.map((scene, i) => (
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
            boxShadow: "0 0 25px #ffea00aa",
            border: "2px solid #ffea00",
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
              color: "#ffea00",
              fontWeight: 800,
              letterSpacing: 2,
              textTransform: "uppercase",
              fontFamily: "Arial, sans-serif",
            }}
          >
            Estabilizador OIS y Lentes 4K
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
            border: "3px solid #ffea00",
            borderRadius: 26,
            padding: "18px 24px",
            textAlign: "center",
            boxShadow: "0 0 35px #ffea0066",
            backdropFilter: "blur(14px)",
          }}
        >
          <div
            style={{
              display: "inline-flex",
              alignItems: "center",
              justifyContent: "center",
              gap: 10,
              background: "linear-gradient(135deg, #ffea00, #00f0ff)",
              padding: "12px 26px",
              borderRadius: 16,
              boxShadow: "0 0 20px #ffea0088",
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
          background: "linear-gradient(90deg, #ffea00, #00f0ff, #10b981)",
          boxShadow: "0 0 20px #ffea00cc",
        }}
      />

      <Audio src={staticFile("volt_voice_reel7.mp3")} volume={1.0} />
      <Audio src={staticFile("bg_music.webm")} volume={0.12} loop />
    </AbsoluteFill>
  );
};
