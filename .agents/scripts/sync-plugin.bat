@echo off
setlocal enabledelayedexpansion

if "%~1"=="" goto usage
if "%~2"=="" goto usage

set "PLUGIN_NAME=%~1"
set "REPO_URL=%~2"
set "TARGET_DIR=.agents\plugins\%PLUGIN_NAME%"
set "TEMP_DIR=temp_sync_%PLUGIN_NAME%"

echo Sincronizzazione del plugin '%PLUGIN_NAME%' da %REPO_URL%...

if exist "%TEMP_DIR%" rmdir /s /q "%TEMP_DIR%"
git clone --depth 1 "%REPO_URL%" "%TEMP_DIR%"
if errorlevel 1 (
    echo [ERRORE] Clonazione fallita. Verifica URL e connessione.
    exit /b 1
)

if exist "%TEMP_DIR%\.git" rmdir /s /q "%TEMP_DIR%\.git"

if not exist "%TARGET_DIR%" mkdir "%TARGET_DIR%"
xcopy /E /Y /I "%TEMP_DIR%\*" "%TARGET_DIR%\" >nul

rmdir /s /q "%TEMP_DIR%"

echo [OK] Plugin '%PLUGIN_NAME%' aggiornato in %TARGET_DIR%.
echo Ricordati di verificare .agents\plugins\plugins.md e aggiornare il log giornaliero (logs\YYYY-MM-DD.log).
endlocal
exit /b 0

:usage
echo Uso: %~nx0 ^<nome-plugin^> ^<url-repo-github^>
exit /b 1