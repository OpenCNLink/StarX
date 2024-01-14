win32command = ['reg add "HKCU\Software\Microsoft\Windows\CurrentVersion\Internet Settings" /v ProxyEnable /t REG_DWORD /d 1 /f >nul 2>nul','reg add "HKCU\Software\Microsoft\Windows\CurrentVersion\Internet Settings" /v ProxyServer /d "{}" /f >nul 2>nul']
unixcommand = ['export http_proxy=http://{}']

import os
import sys

def switchProxy(ip:str,port:int,isopen=False):
    if isopen:
        if sys.platform == 'win32':
            os.system('reg add "HKCU\Software\Microsoft\Windows\CurrentVersion\Internet Settings" /v ProxyEnable /t REG_DWORD /d 0 /f >nul 2>nul')
            os.system('reg add "HKCU\Software\Microsoft\Windows\CurrentVersion\Internet Settings" /v ProxyServer /d "" /f >nul 2>nul')
    else:
        if sys.platform == 'win32':
            for text in win32command:
                os.system(text.format(ip+str(port)))
        else:
            os.sytem(unixcommand[0].format(ip+str(port)))