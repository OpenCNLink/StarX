import logger.fileio
import logger.output

class log:
    def __init__(self,filename='log.txt'):
        self.filename = filename
    
    def write(self,text):
        logger.fileio.writeLog(text,self.filename)
    
    def print(self,text):
        logger.output.printMessage(text)