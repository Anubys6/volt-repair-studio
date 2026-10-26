@echo off
chcp 65001 > nul
title Generador Automatizado de Videos y Reels - Volt Repair Studio
cls
echo ======================================================================
echo    VOLT REPAIR STUDIO - ESTUDIO AUTOMATICO DE VIDEOS Y REELS (9:16)
echo ======================================================================
echo.
echo Iniciando motor de renderizado con Edge-TTS y FFmpeg...
echo.

python "%~dp0videos\reels_generator_volt.py"

echo.
echo ======================================================================
echo  Renderizado completado. Abriendo carpeta de videos generados...
echo ======================================================================
start "" "%~dp0videos\reels_exportados"
pause
