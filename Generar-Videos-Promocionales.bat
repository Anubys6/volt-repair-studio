@echo off
chcp 65001 > nul
title Generador Profesional de Videos y Reels - Volt Repair Studio
cls
echo ======================================================================
echo    VOLT REPAIR STUDIO - ESTUDIO CINEMATOGRAFICO DE REELS (9:16)
echo       Video Real de Fondo + Subtitulos CapCut + Locucion Neural
echo ======================================================================
echo.
echo Iniciando renderizado de alta fidelidad con FFmpeg y Edge-TTS...
echo.

python "%~dp0videos\reels_pro_video_generator.py"

echo.
echo ======================================================================
echo  Renderizado completado. Abriendo carpeta de videos generados...
echo ======================================================================
start "" "%~dp0videos\reels_exportados"
pause
