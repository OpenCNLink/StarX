import time

def formatMessage(text) -> str:
    template = '[INFO] [{}] {}'
    return template.format(str(int(time.time())),text)

def printMessage(text) -> None:
    print(formatMessage(text))
    return
