@echo off
setlocal enabledelayedexpansion

if "%~1"=="" goto usage
if "%~2"=="" goto usage
if "%~3"=="" goto usage

set "JARVIS_ROOT=%~1"
set "PLUGIN_NAME=%~2"
set "REPO_URL=%~3"

if "%JARVIS_ROOT:~-1%"=="\" set "JARVIS_ROOT=%JARVIS_ROOT:~0,-1%"
if "%JARVIS_ROOT:~-1%"=="/" set "JARVIS_ROOT=%JARVIS_ROOT:~0,-1%"

set "TARGET_DIR=%JARVIS_ROOT%\.agents\plugins\%PLUGIN_NAME%"
set "TEMP_DIR=%TEMP%\jarvis_sync_%PLUGIN_NAME%"

echo Sincronizzazione del plugin '%PLUGIN_NAME%' da %REPO_URL%...
echo Cartella di destinazione: %TARGET_DIR%

if exist "%TEMP_DIR%" rmdir /s /q "%TEMP_DIR%"
git clone --depth 1 "%REPO_URL%" "%TEMP_DIR%"
if errorlevel 1 (
    echo [ERRORE] Clonazione fallita. Verifica URL e connessione.
    if exist "%TEMP_DIR%" rmdir /s /q "%TEMP_DIR%"
    exit /b 1
)

echo Removing the .git folder from the temporary directory...
if exist "%TEMP_DIR%\.git" rmdir /s /q "%TEMP_DIR%\.git"

echo checking if target directory exists...
if not exist "%TARGET_DIR%" mkdir "%TARGET_DIR%"

echo Copying files from temporary directory to target directory...
xcopy /E /Y /I "%TEMP_DIR%" "%TARGET_DIR%" >nul
if errorlevel 1 (
    echo [ERRORE] Copia dei file fallita.
    if exist "%TEMP_DIR%" rmdir /s /q "%TEMP_DIR%"
    exit /b 1
)

echo Cleaning up temporary directory...
if exist "%TEMP_DIR%" rmdir /s /q "%TEMP_DIR%"

echo [OK] Plugin '%PLUGIN_NAME%' aggiornato in %TARGET_DIR%.
echo Ricordati di verificare .agents\plugins\plugins.md e aggiornare il log giornaliero (logs\YYYY-MM-DD.log).
endlocal
exit /b 0

:usage
echo Uso: %~nx0 ^<jarvisroot-folder^> ^<nome-plugin^> ^<url-repo-github^>
exit /b 1
