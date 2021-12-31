import base64
#from pwntools import *
import codecs
def base64(str1, state):
    if state == 'enc':
        return str(base64.b64encode(str1.encode("utf-8")), 'utf-8')
    else:
        return str(base64.b64decode(str1.encode("utf-8")), 'utf-8')

def base32(str1, state):
    if state == 'enc':
        return str(base64.b32encode(str1.encode("utf-8")), 'utf-8')
    else:
        return str(base64.b32decode(str1.encode("utf-8")), 'utf-8')

def base16(str1, state):
    if state == 'enc':
        return str(base64.b16encode(str1.encode("utf-8")), 'utf-8')
    else:
        return str(base64.b16decode(str1.encode("utf-8")), 'utf-8')

def hex(str1, state):
    if state == 'enc':
        return 'not workin, sorry'
    else:
        return unhex(str1)

def rot13(str1, state):
    if state == 'enc':
        return codecs.encode(str1, 'rot_13')
    else:
        return codecs.decode(str1, 'rot_13')
