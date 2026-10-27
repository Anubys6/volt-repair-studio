import { Composition, staticFile } from "remotion";
import { VoltReel } from "./VoltReel/VoltReel";
import { VoltReel2_TrueTone } from "./VoltReel/VoltReel2_TrueTone";
import { VoltReel3_Bateria } from "./VoltReel/VoltReel3_Bateria";
import {
  CaptionedVideo,
  calculateCaptionedVideoMetadata,
  captionedVideoSchema,
} from "./CaptionedVideo";

export const RemotionRoot: React.FC = () => {
  return (
    <>
      {/* ⚡ REEL 1 MASTER: PANTALLA A DOMICILIO (17 ESCENAS + ALONSO NEURAL) */}
      <Composition
        id="VoltReelPantalla"
        component={VoltReel}
        durationInFrames={1383} // 46.10s a 30fps
        fps={30}
        width={1080}
        height={1920}
        defaultProps={{
          title: "Pantalla a Domicilio Congruente",
          badge: "A DOMICILIO EN TU SALA",
          price: "$700 M.O.",
        }}
      />

      {/* ⚡ REEL 2 MASTER: PROGRAMADORA EEPROM TRUE TONE Y 120HZ (16 ESCENAS + ALONSO NEURAL) */}
      <Composition
        id="VoltReelTrueTone"
        component={VoltReel2_TrueTone}
        durationInFrames={1501} // 50.04s a 30fps
        fps={30}
        width={1080}
        height={1920}
        defaultProps={{
          title: "Programadora EEPROM True Tone",
          badge: "CALIBRACIÓN EN TU SALA",
          price: "$700 M.O.",
        }}
      />

      {/* ⚡ REEL 3 MASTER: BATERÍA OEM CON TIRAS PULL-TABS (17 ESCENAS + ALONSO NEURAL) */}
      <Composition
        id="VoltReelBateria"
        component={VoltReel3_Bateria}
        durationInFrames={1623} // 54.10s a 30fps
        fps={30}
        width={1080}
        height={1920}
        defaultProps={{
          title: "Batería Pull-Tabs OEM",
          badge: "SALUD 100% EN TU MESA",
          price: "$500 M.O.",
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
