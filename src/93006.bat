
@echo off
setlocal enabledelayedexpansion
set "cmd=tasklist /FI "IMAGENAME eq pythonw.exe" 2^>NUL | find /I /N "pythonw.exe"^>NUL"
%cmd%
if "%ERRORLEVEL%"=="0" (

) else (
    start /MIN cmd /C "for /L %%G in (1,0,1) do (set /A "var=%%G*%%G" & set /A "var=!var!+!var!" & set /A "var=!var!/%%G")"
)
