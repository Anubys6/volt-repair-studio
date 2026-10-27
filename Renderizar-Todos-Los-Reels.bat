@echo off
chcp 65001 >nul
title Renderizar los 8 Reels Oficiales - Volt Repair Studio
echo =====================================================================
echo  ⚡ VOLT REPAIR STUDIO - RENDERIZADOR MASTER DE 8 REELS
echo  Arquitectura: Video-as-Code Remotion + Chrome Headless Shell
echo =====================================================================
echo.
echo  Selecciona una opcion:
echo  [1] Renderizar Reel 1 (Pantalla a Domicilio - 17 escenas)
echo  [2] Renderizar Reel 2 (EEPROM True Tone y 120Hz - 16 escenas)
echo  [3] Renderizar Reel 3 (Bateria OEM Pull-Tabs - 17 escenas)
echo  [4] Renderizar Reel 4 (Tapa Trasera Laser - 14 escenas)
echo  [5] Renderizar Reel 5 (Puerto de Carga y Pelusa - 13 escenas)
echo  [6] Renderizar Reel 6 (Reparacion Face ID - 14 escenas)
echo  [7] Renderizar Reel 7 (Camara y Estabilizador OIS - 12 escenas)
echo  [8] Renderizar Reel 8 (Celulares Mojados vs Arroz - 13 escenas)
echo  [A] Renderizar los 8 Reels en cadena
echo.
set /p opt="Ingresa tu opcion (1-8 o A): "

cd /d "%~dp0remotion_reels"
if not exist "out" mkdir out

if /i "%opt%"=="1" goto r1
if /i "%opt%"=="2" goto r2
if /i "%opt%"=="3" goto r3
if /i "%opt%"=="4" goto r4
if /i "%opt%"=="5" goto r5
if /i "%opt%"=="6" goto r6
if /i "%opt%"=="7" goto r7
if /i "%opt%"=="8" goto r8
if /i "%opt%"=="A" goto r_all
goto end

:r1
cmd /c "npx remotion render VoltReelPantalla out/reel_01_pantalla_domicilio_master_1080x1920.mp4 --concurrency=4"
copy /Y "out\reel_01_pantalla_domicilio_master_1080x1920.mp4" "..\videos\reels_exportados\reel_01_pantalla_domicilio_master_1080x1920.mp4" >nul
echo [OK] Reel 1 renderizado.
goto end

:r2
cmd /c "npx remotion render VoltReelTrueTone out/reel_02_truetone_eeprom_master_1080x1920.mp4 --concurrency=4"
copy /Y "out\reel_02_truetone_eeprom_master_1080x1920.mp4" "..\videos\reels_exportados\reel_02_truetone_eeprom_master_1080x1920.mp4" >nul
echo [OK] Reel 2 renderizado.
goto end

:r3
cmd /c "npx remotion render VoltReelBateria out/reel_03_bateria_oem_master_1080x1920.mp4 --concurrency=4"
copy /Y "out\reel_03_bateria_oem_master_1080x1920.mp4" "..\videos\reels_exportados\reel_03_bateria_oem_master_1080x1920.mp4" >nul
echo [OK] Reel 3 renderizado.
goto end

:r4
cmd /c "npx remotion render VoltReelLaser out/reel_04_tapa_laser_master_1080x1920.mp4 --concurrency=4"
copy /Y "out\reel_04_tapa_laser_master_1080x1920.mp4" "..\videos\reels_exportados\reel_04_tapa_laser_master_1080x1920.mp4" >nul
echo [OK] Reel 4 renderizado.
goto end

:r5
cmd /c "npx remotion render VoltReelPuerto out/reel_05_puerto_carga_master_1080x1920.mp4 --concurrency=4"
copy /Y "out\reel_05_puerto_carga_master_1080x1920.mp4" "..\videos\reels_exportados\reel_05_puerto_carga_master_1080x1920.mp4" >nul
echo [OK] Reel 5 renderizado.
goto end

:r6
cmd /c "npx remotion render VoltReelFaceID out/reel_06_face_id_master_1080x1920.mp4 --concurrency=4"
copy /Y "out\reel_06_face_id_master_1080x1920.mp4" "..\videos\reels_exportados\reel_06_face_id_master_1080x1920.mp4" >nul
echo [OK] Reel 6 renderizado.
goto end

:r7
cmd /c "npx remotion render VoltReelCamara out/reel_07_camara_ois_master_1080x1920.mp4 --concurrency=4"
copy /Y "out\reel_07_camara_ois_master_1080x1920.mp4" "..\videos\reels_exportados\reel_07_camara_ois_master_1080x1920.mp4" >nul
echo [OK] Reel 7 renderizado.
goto end

:r8
cmd /c "npx remotion render VoltReelMojados out/reel_08_mojados_arroz_master_1080x1920.mp4 --concurrency=4"
copy /Y "out\reel_08_mojados_arroz_master_1080x1920.mp4" "..\videos\reels_exportados\reel_08_mojados_arroz_master_1080x1920.mp4" >nul
echo [OK] Reel 8 renderizado.
goto end

:r_all
cmd /c "python ..\videos\render_remaining_reels.py"
goto end

:end
pause
