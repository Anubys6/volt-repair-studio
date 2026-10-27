import React from "react";
import {
  AbsoluteFill,
  Audio,
  Img,
  interpolate,
  OffthreadVideo,
  spring,
  staticFile,
  useCurrentFrame,
  useVideoConfig,
} from "remotion";

export interface VoltReelProps {
  title: string;
  badge: string;
  price: string;
  hookText: string;
  solutionText: string;
  ctaText: string;
  phone: string;
}

export const VoltReel: React.FC<VoltReelProps> = ({
  badge = "A DOMICILIO EN TU SALA",
  price = "$700 M.O.",
  hookText = "¿POR QUÉ LE TIENEN TANTO MIEDO A LOS TALLERES?",
  solutionText = "Reparación frente a tus ojos en 25 minutos. Cero fotos revisadas, refacciones 100% garantizadas.",
  ctaText = "Mándanos WhatsApp y cotiza tu modelo hoy",
  phone = "+52 1 720 815 7790",
}) => {
  const frame = useCurrentFrame();
  const { fps, durationInFrames, width, height } = useVideoConfig();

  // Animaciones de entrada (Springs con física suave)
  const headerEntrance = spring({
    frame,
    fps,
    config: { damping: 200, mass: 0.5 },
  });

  const badgeEntrance = spring({
    frame: frame - 10,
    fps,
    config: { damping: 180, mass: 0.6 },
  });

  const hookEntrance = spring({
    frame: frame - 25,
    fps,
    config: { damping: 150, mass: 0.8 },
  });

  const ctaPulse = interpolate(
    Math.sin((frame / fps) * 4),
    [-1, 1],
    [0.98, 1.02]
  );

  // Barra de progreso inferior
  const progressWidth = interpolate(frame, [0, durationInFrames], [0, width], {
    extrapolateRight: "clamp",
  });

  return (
    <AbsoluteFill style={{ backgroundColor: "#060911" }}>
      {/* 1. Fondo de Video en Movimiento */}
      <AbsoluteFill>
        <OffthreadVideo
          src={staticFile("broll_pantalla.mp4")}
          style={{
            width: "100%",
            height: "100%",
            objectFit: "cover",
          }}
        />
      </AbsoluteFill>

      {/* 2. Viñeta Cinematográfica Suave (Para legibilidad de textos) */}
      <AbsoluteFill
        style={{
          background:
            "linear-gradient(180deg, rgba(6, 9, 17, 0.88) 0%, rgba(6, 9, 17, 0.15) 30%, rgba(6, 9, 17, 0.15) 65%, rgba(6, 9, 17, 0.94) 100%)",
        }}
      />

      {/* 3. Header Superior Flotante: Logo y Marca */}
      <div
        style={{
          position: "absolute",
          top: 70,
          left: 0,
          right: 0,
          display: "flex",
          justifyContent: "center",
          alignItems: "center",
          gap: 18,
          transform: `translateY(${interpolate(headerEntrance, [0, 1], [-80, 0])}px)`,
          opacity: headerEntrance,
        }}
      >
        <Img
          src={staticFile("logo.jpg")}
          style={{
            width: 72,
            height: 72,
            borderRadius: 18,
            boxShadow: "0 0 25px rgba(0, 240, 255, 0.6)",
            border: "2px solid #00f0ff",
          }}
        />
        <div>
          <h1
            style={{
              margin: 0,
              fontSize: 42,
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
              fontSize: 22,
              color: "#00f0ff",
              fontWeight: 800,
              letterSpacing: 2,
              textTransform: "uppercase",
              fontFamily: "Arial, sans-serif",
            }}
          >
            Servicio Técnico Certificado
          </span>
        </div>
      </div>

      {/* 4. Badge Neón con Precio de Mano de Obra */}
      <div
        style={{
          position: "absolute",
          top: 190,
          left: 0,
          right: 0,
          display: "flex",
          justifyContent: "center",
          transform: `scale(${interpolate(badgeEntrance, [0, 1], [0.6, 1])})`,
          opacity: badgeEntrance,
        }}
      >
        <div
          style={{
            background: "linear-gradient(135deg, #00f0ff 0%, #0077ff 100%)",
            padding: "14px 38px",
            borderRadius: 50,
            display: "flex",
            alignItems: "center",
            gap: 16,
            boxShadow: "0 0 35px rgba(0, 240, 255, 0.55)",
          }}
        >
          <span
            style={{
              fontSize: 26,
              fontWeight: 900,
              color: "#050914",
              fontFamily: "Arial Black, sans-serif",
              letterSpacing: 1,
            }}
          >
            ⚡ {badge}
          </span>
          <span
            style={{
              background: "#050914",
              color: "#ffea00",
              padding: "4px 16px",
              borderRadius: 30,
              fontSize: 24,
              fontWeight: 900,
              fontFamily: "Arial Black, sans-serif",
            }}
          >
            {price}
          </span>
        </div>
      </div>

      {/* 5. Gancho Principal de Impacto (Centro Superior) */}
      <div
        style={{
          position: "absolute",
          top: 310,
          left: 60,
          right: 60,
          textAlign: "center",
          transform: `translateY(${interpolate(hookEntrance, [0, 1], [40, 0])}px)`,
          opacity: hookEntrance,
        }}
      >
        <h2
          style={{
            fontSize: 56,
            fontWeight: 900,
            color: "#ffffff",
            textTransform: "uppercase",
            fontFamily: "Arial Black, sans-serif",
            lineHeight: 1.15,
            margin: 0,
            WebkitTextStroke: "6px #000000",
            paintOrder: "stroke fill",
            textShadow: "0 8px 30px rgba(0,0,0,0.9)",
          }}
        >
          {hookText}
        </h2>
      </div>

      {/* 6. Caja Inferior de Llamado a la Acción y Contacto */}
      <div
        style={{
          position: "absolute",
          bottom: 110,
          left: 50,
          right: 50,
          transform: `scale(${ctaPulse})`,
        }}
      >
        <div
          style={{
            background: "rgba(14, 20, 36, 0.94)",
            border: "3px solid #00f0ff",
            borderRadius: 28,
            padding: "26px 32px",
            textAlign: "center",
            boxShadow: "0 0 40px rgba(0, 240, 255, 0.35)",
            backdropFilter: "blur(12px)",
          }}
        >
          <p
            style={{
              fontSize: 28,
              color: "#cbd5e1",
              margin: "0 0 16px 0",
              fontWeight: 700,
              fontFamily: "Arial, sans-serif",
              lineHeight: 1.35,
            }}
          >
            {solutionText}
          </p>
          <div
            style={{
              display: "flex",
              justifyContent: "center",
              alignItems: "center",
              gap: 12,
              background: "linear-gradient(135deg, #00f0ff, #0055ff)",
              padding: "14px 24px",
              borderRadius: 18,
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
              📲 WhatsApp: {phone}
            </span>
          </div>
          <p
            style={{
              margin: "12px 0 0 0",
              fontSize: 22,
              color: "#94a3b8",
              fontWeight: 800,
              fontFamily: "Arial, sans-serif",
            }}
          >
            🛡️ 90 Días de Garantía por Escrito | @voltrepair32
          </p>
        </div>
      </div>

      {/* 7. Barra de Progreso Inferior */}
      <div
        style={{
          position: "absolute",
          bottom: 0,
          left: 0,
          height: 14,
          width: `${progressWidth}px`,
          background: "linear-gradient(90deg, #00f0ff, #ff0055, #ffea00)",
          boxShadow: "0 0 15px rgba(0, 240, 255, 0.8)",
        }}
      />

      {/* 8. Pistas de Audio Sincronizadas */}
      <Audio src={staticFile("volt_voice_1.mp3")} volume={1.0} />
      <Audio src={staticFile("bg_music.webm")} volume={0.15} loop />
    </AbsoluteFill>
  );
};
