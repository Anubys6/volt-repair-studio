@echo off
chcp 65001 >nul
title Remotion Studio - Volt Repair Studio
echo =====================================================================
echo  ⚡ REMOTION STUDIO - EDICION PROGRAMATICA DE VIDEO (VIDEO-AS-CODE)
echo =====================================================================
echo.
echo Iniciando servidor de previsualizacion en vivo...
cd /d "%~dp0remotion_reels"
start "" http://localhost:3000
cmd /c "npm run dev"
pause
