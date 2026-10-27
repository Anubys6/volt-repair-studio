@echo off
chcp 65001 >nul
title Renderizar Video con Remotion - Volt Repair Studio
echo =====================================================================
echo  ⚡ EXPORTACION DE VIDEO REMOTION MASTER MP4 (1080x1920)
echo  Arquitectura: Video-as-Code React con 17 escenas congruentes en movimiento continuo
echo =====================================================================
echo.
cd /d "%~dp0remotion_reels"
if not exist "out" mkdir out
echo Renderizando VoltReelPantalla con Chrome Headless Shell a 30 FPS Master...
cmd /c "npx remotion render VoltReelPantalla out/reel_remotion_congruente_amigable_1080x1920.mp4 --concurrency=4"
if %ERRORLEVEL% EQU 0 (
    copy /Y "out\reel_remotion_congruente_amigable_1080x1920.mp4" "..\videos\reels_exportados\reel_remotion_congruente_amigable_1080x1920.mp4" >nul
    echo.
    echo =====================================================================
    echo  ✅ Video exportado con exito en:
    echo     1. remotion_reels\out\reel_remotion_congruente_amigable_1080x1920.mp4
    echo     2. videos\reels_exportados\reel_remotion_congruente_amigable_1080x1920.mp4
    echo =====================================================================
) else (
    echo.
    echo ❌ Ocurrio un error en el renderizado de Remotion.
)
pause
