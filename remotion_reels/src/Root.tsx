import { Composition, staticFile } from "remotion";
import { VoltReel } from "./VoltReel/VoltReel";
import { VoltReel2_TrueTone } from "./VoltReel/VoltReel2_TrueTone";
import { VoltReel3_Bateria } from "./VoltReel/VoltReel3_Bateria";
import { VoltReel4_Laser } from "./VoltReel/VoltReel4_Laser";
import { VoltReel5_Puerto } from "./VoltReel/VoltReel5_Puerto";
import { VoltReel6_FaceID } from "./VoltReel/VoltReel6_FaceID";
import { VoltReel7_Camara } from "./VoltReel/VoltReel7_Camara";
import { VoltReel8_Mojados } from "./VoltReel/VoltReel8_Mojados";
import {
  CaptionedVideo,
  calculateCaptionedVideoMetadata,
  captionedVideoSchema,
} from "./CaptionedVideo";

export const RemotionRoot: React.FC = () => {
  return (
    <>
      {/* ⚡ REEL 1: PANTALLA A DOMICILIO ($700 M.O.) */}
      <Composition
        id="VoltReelPantalla"
        component={VoltReel}
        durationInFrames={1383}
        fps={30}
        width={1080}
        height={1920}
      />

      {/* ⚡ REEL 2: EEPROM TRUE TONE Y 120HZ ($700 M.O.) */}
      <Composition
        id="VoltReelTrueTone"
        component={VoltReel2_TrueTone}
        durationInFrames={1501}
        fps={30}
        width={1080}
        height={1920}
      />

      {/* ⚡ REEL 3: BATERÍA OEM PULL-TABS ($500 M.O.) */}
      <Composition
        id="VoltReelBateria"
        component={VoltReel3_Bateria}
        durationInFrames={1623}
        fps={30}
        width={1080}
        height={1920}
      />

      {/* ⚡ REEL 4: TAPA TRASERA MÁQUINA LÁSER ($500 M.O.) */}
      <Composition
        id="VoltReelLaser"
        component={VoltReel4_Laser}
        durationInFrames={1654}
        fps={30}
        width={1080}
        height={1920}
      />

      {/* ⚡ REEL 5: LIMPIEZA DE PUERTO DE CARGA ($300 M.O.) */}
      <Composition
        id="VoltReelPuerto"
        component={VoltReel5_Puerto}
        durationInFrames={1746}
        fps={30}
        width={1080}
        height={1920}
      />

      {/* ⚡ REEL 6: REPARACIÓN DE FACE ID DOT PROJECTOR ($700 M.O.) */}
      <Composition
        id="VoltReelFaceID"
        component={VoltReel6_FaceID}
        durationInFrames={1874}
        fps={30}
        width={1080}
        height={1920}
      />

      {/* ⚡ REEL 7: CÁMARA Y ESTABILIZADOR OIS ($600 M.O.) */}
      <Composition
        id="VoltReelCamara"
        component={VoltReel7_Camara}
        durationInFrames={1663}
        fps={30}
        width={1080}
        height={1920}
      />

      {/* ⚡ REEL 8: CELULARES MOJADOS VS MITO DEL ARROZ ($500 M.O.) */}
      <Composition
        id="VoltReelMojados"
        component={VoltReel8_Mojados}
        durationInFrames={1890}
        fps={30}
        width={1080}
        height={1920}
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
