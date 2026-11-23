@echo off
setlocal enabledelayedexpansion

if "%~1"=="" (
    for %%I in ("%~dp0..\..") do set "JARVIS_ROOT=%%~fI"
) else (
    set "JARVIS_ROOT=%~1"
)

if "%JARVIS_ROOT:~-1%"=="\" set "JARVIS_ROOT=%JARVIS_ROOT:~0,-1%"
if "%JARVIS_ROOT:~-1%"=="/" set "JARVIS_ROOT=%JARVIS_ROOT:~0,-1%"

echo All Plugin Sync started...
echo Jarvis Root Folder: %JARVIS_ROOT%
call "%JARVIS_ROOT%\.agents\scripts\sync-plugin.bat" "%JARVIS_ROOT%" enterprise-architect https://github.com/fgaravaglia/EnterpriseArchitectSystemPrompts.git 

echo All Plugin Sync Completed.
endlocal
exit /b 0

:usage
echo Uso: %~nx0 [Jarvis Root Folder]
exit /b 1
