@echo off
chcp 65001 >nul
title Renderizar Video con Remotion
echo =====================================================================
echo  ⚡ EXPORTACION DE VIDEO REMOTION MP4 (1080x1920)
echo =====================================================================
echo.
cd /d "%~dp0remotion_reels"
if not exist "out" mkdir out
echo Renderizando con Chrome Headless Shell a 60 FPS...
cmd /c "npx remotion render CaptionedVideo out/reel_remotion_tiktok_1080x1920.mp4 --gl=angle"
echo.
echo =====================================================================
echo  ✅ Video exportado en: remotion_reels\out\reel_remotion_tiktok_1080x1920.mp4
echo =====================================================================
pause
