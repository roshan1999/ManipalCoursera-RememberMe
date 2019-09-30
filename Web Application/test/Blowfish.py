from Crypto.Cipher import Blowfish
from struct import pack

bs = Blowfish.block_size
key = b'An arbitary length key'
cipher = Blowfish.new(key, Blowfish.MODE_CBC)
plaintext = b'Ben_dOver'
plen = bs - len(plaintext) % bs
padding = [plen]*plen
padding = pack('b'*plen, *padding)
msg = cipher.iv + cipher.encrypt(plaintext + padding)
print(msg)
