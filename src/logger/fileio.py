def writeLog(text,filename) -> bool:
    try:
        with open(filename,'a') as f:
            f.write(text)
        return True
    except:
        return False