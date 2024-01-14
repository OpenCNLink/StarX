def writeLog(text,filename='log.txt') -> bool:
    try:
        with open(filename,'a') as f:
            f.write(text)
        return True
    except:
        return False