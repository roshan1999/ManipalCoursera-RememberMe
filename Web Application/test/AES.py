from Crypto.Cipher import AES

key = b'Sixteen byte key'
cipher = AES.new(key, AES.MODE_EAX)
nonce = cipher.nonce
plaintext = b'aishaLove'
ciphertext, tag = cipher.encrypt_and_digest(plaintext)
print(ciphertext)
