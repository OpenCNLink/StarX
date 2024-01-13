import sys
import hashlib

def get_md5(data):
    obj = hashlib.md5(sys.platform.encode('utf-8'))
    obj.update(data.encode('utf-8'))
    result = obj.hexdigest()
    return result