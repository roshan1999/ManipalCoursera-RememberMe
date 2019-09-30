    import random
    import string
    def randomString(stringLength):
        """Generate a random string with the combination of lowercase and uppercase letters """
        letters = string.ascii_letters
        return ''.join(random.choice(letters) for i in range(stringLength))
    print("Random String with the combination of lowercase and uppercase letters")
    print ("First Random String is ", randomString(8) )
    print ("second Random String is ", randomString(8) )



    import onetimepad

cipher = onetimepad.encrypt('One Time Cipher', 'random')
print("Cipher text is ")
print(cipher)
print("Plain text is ")
msg = onetimepad.decrypt(cipher, 'random')

print(msg)