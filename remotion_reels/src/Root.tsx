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
      {/* ⚡ COMPOSICIÓN VIRAL OFICIAL DE VOLT REPAIR STUDIO */}
      <Composition
        id="VoltReelPantalla"
        component={VoltReel}
        durationInFrames={30 * 31}
        fps={30}
        width={1080}
        height={1920}
        defaultProps={{
          title: "Pantalla a Domicilio",
          badge: "A DOMICILIO EN TU SALA",
          price: "$700 M.O.",
          hookText: "¿POR QUÉ LE TIENEN TANTO MIEDO A LOS TALLERES?",
          solutionText:
            "Reparación en tu propia sala en 25 minutos. Cero fotos revisadas, refacciones 100% garantizadas.",
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
