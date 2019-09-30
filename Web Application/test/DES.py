from Crypto.Cipher import DES
from Crypto.Random import get_random_bytes
from rsa_encrypt import *

def des(key,plaintext):
    if key is None:
        key =  get_random_bytes(8)
    print(key)
    cipher = DES.new(key, DES.MODE_OFB)
    #plaintext = b'sona si latine loqueris '
    plaintext = plaintext.encode()
    msg = cipher.iv + cipher.encrypt(plaintext)
    return key,msg
