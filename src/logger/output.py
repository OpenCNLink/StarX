import time

def formatMessage(text) -> str:
    template = '[INFO] [Unixtime:{}] {}'
    return template.format(str(time.time()),text)

def printMessage(text) -> None:
    print(formatMessage(text))
    return
