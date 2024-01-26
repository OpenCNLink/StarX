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
    warnList = ['wechat.exe','qq.exe','imeutil.exe','Mbbmanager.exe','Runouce.exe','Winmsg32.exe']
    while True:
        # Task 1: 进程列表监控
        x = os.popen('tasklist').read()
        for i in blackList:
            if i in x:
                for blacker in blackList:
                showLog('发现被拉黑进程:{}，已进行 结束 操作.'.format(blacker))
                os.system('taskkill /f /im {}'.format(blacker))
        for i in warnlist:
            if i in warnList:
                for warner in warnList:
                    showLog('警告: 风险进程 {} 正在运行.'.format(warner))