@echo off

setlocal
if exist "%~dp0\python.exe" (
    "%~dp0\python" "%~dp0rodm" %*
) else (
    "%~dp0..\python" "%~dp0rodm" %*
)
endlocal