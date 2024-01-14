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
        
print('StarX version 0.1.0 - Run on {}'.format(system.info.sysInfo.python))
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
    except KeyboardInterrupt:
        network.proxy.switchProxy('127.0.0.1','2111',True)