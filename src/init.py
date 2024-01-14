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
while True:
    showLog = logger.log()
    try:
        showLog.print('Started StarX')
        showLog.print('Checking server......')
        x = network.http.canopen(server)
        if not x:
            raise RuntimeError('Cannot client to StarX server')
        else:
            showLog.print('The connection to the server is normal')
        import json
        import urllib.request
        handshake = {
            'version':'0.1.0',
            'token':hpassword
        }
        handshake = json.dump(handshake)
        headers = {'Accept-Charset': 'utf-8', 'Content-Type': 'application/json'}
        req = urllib.request.Request(url=server+'/api/v2/handshake', data=handshake, headers=headers, method='POST')
        response = urllib.request.urlopen(req).read()
        if not bool(response):raise RuntimeError('Cannot client to StarX server')
        showLog.print('A daemon is being created')
    except KeyboardInterrupt:
        network.proxy.switchProxy('127.0.0.1','2111',True)