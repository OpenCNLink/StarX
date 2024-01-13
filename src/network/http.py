import urllib.request

def canopen(url:str) -> bool:
    try:
        urllib.request.urlopen(url)
        return True
    except: return False