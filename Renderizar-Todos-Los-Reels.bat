@echo off
chcp 65001 >nul
title Renderizar los 3 Reels Oficiales - Volt Repair Studio
echo =====================================================================
echo  ⚡ VOLT REPAIR STUDIO - RENDERIZADOR MASTER DE 3 REELS
echo  Arquitectura: Video-as-Code Remotion + Chrome Headless Shell
echo =====================================================================
echo.
echo  Selecciona una opcion:
echo  [1] Renderizar Reel 1 (Pantalla a Domicilio - 17 escenas)
echo  [2] Renderizar Reel 2 (EEPROM True Tone y 120Hz - 16 escenas)
echo  [3] Renderizar Reel 3 (Bateria OEM Pull-Tabs - 17 escenas)
echo  [4] Renderizar los 3 Reels en cadena
echo.
set /p opt="Ingresa tu opcion (1-4): "

cd /d "%~dp0remotion_reels"
if not exist "out" mkdir out

if "%opt%"=="1" goto reel1
if "%opt%"=="2" goto reel2
if "%opt%"=="3" goto reel3
if "%opt%"=="4" goto reel_all
goto end

:reel1
echo.
echo [1/1] Renderizando Reel 1: Pantalla a Domicilio...
cmd /c "npx remotion render VoltReelPantalla out/reel_01_pantalla_domicilio_master_1080x1920.mp4 --concurrency=4"
copy /Y "out\reel_01_pantalla_domicilio_master_1080x1920.mp4" "..\videos\reels_exportados\reel_01_pantalla_domicilio_master_1080x1920.mp4" >nul
echo ✅ Reel 1 completado.
goto end

:reel2
echo.
echo [1/1] Renderizando Reel 2: EEPROM True Tone y 120Hz...
cmd /c "npx remotion render VoltReelTrueTone out/reel_02_truetone_eeprom_master_1080x1920.mp4 --concurrency=4"
copy /Y "out\reel_02_truetone_eeprom_master_1080x1920.mp4" "..\videos\reels_exportados\reel_02_truetone_eeprom_master_1080x1920.mp4" >nul
echo ✅ Reel 2 completado.
goto end

:reel3
echo.
echo [1/1] Renderizando Reel 3: Bateria OEM Pull-Tabs...
cmd /c "npx remotion render VoltReelBateria out/reel_03_bateria_oem_master_1080x1920.mp4 --concurrency=4"
copy /Y "out\reel_03_bateria_oem_master_1080x1920.mp4" "..\videos\reels_exportados\reel_03_bateria_oem_master_1080x1920.mp4" >nul
echo ✅ Reel 3 completado.
goto end

:reel_all
echo.
echo [1/3] Renderizando Reel 1: Pantalla a Domicilio...
cmd /c "npx remotion render VoltReelPantalla out/reel_01_pantalla_domicilio_master_1080x1920.mp4 --concurrency=4"
copy /Y "out\reel_01_pantalla_domicilio_master_1080x1920.mp4" "..\videos\reels_exportados\reel_01_pantalla_domicilio_master_1080x1920.mp4" >nul

echo.
echo [2/3] Renderizando Reel 2: EEPROM True Tone y 120Hz...
cmd /c "npx remotion render VoltReelTrueTone out/reel_02_truetone_eeprom_master_1080x1920.mp4 --concurrency=4"
copy /Y "out\reel_02_truetone_eeprom_master_1080x1920.mp4" "..\videos\reels_exportados\reel_02_truetone_eeprom_master_1080x1920.mp4" >nul

echo.
echo [3/3] Renderizando Reel 3: Bateria OEM Pull-Tabs...
cmd /c "npx remotion render VoltReelBateria out/reel_03_bateria_oem_master_1080x1920.mp4 --concurrency=4"
copy /Y "out\reel_03_bateria_oem_master_1080x1920.mp4" "..\videos\reels_exportados\reel_03_bateria_oem_master_1080x1920.mp4" >nul

echo.
echo =====================================================================
echo  ✅ Los 3 Reels Master fueron exportados con exito a:
echo     C:\Users\SAmue\Desktop\Volt-Repair-Studio\videos\reels_exportados\
echo =====================================================================
goto end

:end
pause
