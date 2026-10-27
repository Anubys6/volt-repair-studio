import { Composition, staticFile } from "remotion";
import { VoltReel } from "./VoltReel/VoltReel";
import {
  CaptionedVideo,
  calculateCaptionedVideoMetadata,
  captionedVideoSchema,
} from "./CaptionedVideo";

export const RemotionRoot: React.FC = () => {
  return (
    <>
      {/* ⚡ COMPOSICIÓN VIRAL OFICIAL DE VOLT REPAIR STUDIO (17 ESCENAS CONGRUENTES + VOZ AMISTOSA) */}
      <Composition
        id="VoltReelPantalla"
        component={VoltReel}
        durationInFrames={1383} // 46.10s a 30fps sincronizado milimétricamente con la locución
        fps={30}
        width={1080}
        height={1920}
        defaultProps={{
          title: "Pantalla a Domicilio Congruente",
          badge: "A DOMICILIO EN TU SALA",
          price: "$700 M.O.",
          hookText: "¿SE TE ESTRELLÓ LA PANTALLA?",
          solutionText:
            "Reparación en tu propio comedor en 25 minutos. Cero fotos revisadas, refacciones Grado A+ garantizadas.",
          ctaText: "Mándanos WhatsApp y cotiza tu modelo hoy",
          phone: "+52 1 720 815 7790",
        }}
      />

      {/* ⚡ PLANTILLA CON SUBTÍTULOS AUTOMÁTICOS WHISPER TIKTOK */}
      <Composition
        id="CaptionedVideo"
        component={CaptionedVideo}
        calculateMetadata={calculateCaptionedVideoMetadata}
        schema={captionedVideoSchema}
        width={1080}
        height={1920}
        defaultProps={{
          src: staticFile("broll_pantalla.mp4"),
        }}
      />
    </>
  );
};
