# -*- coding: utf-8 -*-

from PIL import Image
from Crypto.Cipher import AES
import binascii
import hashlib
import time

# import random


def encryption(password):
    password = hashlib.sha256(password.encode('utf-8')).digest()
    print(password)
    plaintext = []
    plaintextstr = ""

    # random_value = random.randint(100,200)
    # print(random_value)
    im = Image.open('test_image.jpg', 'r')
    arr = im.load()
    print("Image loaded")
    print(im)
    print(arr)
    width, height = im.size
    print(im.size)
    print(width, height)
    # width = im.size[0]  # get width
    # height = im.size[1] # get height

    for y in range(0, height):
        for x in range(0, width):
            plaintext.extend(list(arr[x, y]))
            # plaintext.append(arr[x, y]) # append horizontal rgb tuples
    plaintext = str(''.join(str(x) for x in list(map(lambda x:x+202, plaintext))))

    # print(plaintext)
    print(len(plaintext))   # image length equals to width * height


    plaintext+="w"+str(width)+"w"+"h"+str(height)+"h"
    print(len(plaintext))
    while (len(plaintext) % 16 != 0):
        plaintext = plaintext + "z"
    print(len(plaintext))

    obj = AES.new(password, AES.MODE_CBC, 'This is an IV456')
    ciphertext = obj.encrypt(plaintext)

    print(len(ciphertext))
    print(ciphertext)
    print(len(ciphertext) % 16)
    # print()
    # print()
    cipher_name = "cryptoimg.crypt"
    with open(cipher_name, 'wb') as g:
        g.write((ciphertext))

    # asciicipher = binascii.hexlify(ciphertext)
    # print(ascii(asciicipher))


def decryption(password):
    with open("cryptoimg.crypt", "rb") as crypt_file:
        # crypt_file = open("cryptoimg.crypt", 'rb')
        crypt_file = crypt_file.read()
        # crypt_file = crypt_file.decode('utf-8')
        # print(crypt_file)
        # print(crypt_file[:])
        # print(len(crypt_file) % 16)

        password = hashlib.sha256(password.encode('utf-8')).digest()

        obj = AES.new(password, AES.MODE_CBC, 'This is an IV456')
        # print(len(crypt_file))
        # ciphertext = str(obj.decrypt(crypt_file))
        ciphertext = (obj.decrypt(crypt_file))
        ciphertext = ciphertext.decode('utf-8')
        print('..')

        # print(ciphertext)
        print('.....')
        print(type(ciphertext))
        ciphertext = ciphertext.replace('z', '')
        width = ciphertext.split('w')[1]
        height = ciphertext.split('h')[1]
        widthstr = "w" + str(width) + "w"
        heightstr = "h" + str(height) + "h"
        decrypted = ciphertext.replace(heightstr, "")
        decrypted = decrypted.replace(widthstr, "")
        # decrypted = str(decrypted, 'utf-8')
        # decrypted = decrypted.decode('utf-8')
        print(type(decrypted))
        # print(decrypted)
        print('processing...')
        t = time.time()
        zz = [int(decrypted[i:i+3]) for i in range(0, len(decrypted), 3)]
        print(time.time() - t)

        t2 = time.time()
        finaltexttwo = [((zz[(i)]) - 202, (zz[(i + 1)]) - 202, (zz[(i + 2)]) - 202) for i in range(0, len(zz), 3)]
        print(time.time() - t2)

        # t1 = time.time()
        # zz = tuple(tuple(zz)[i:i + 3] for i in range(0, len(zz), 3))
        # print(time.time() - t1)

        print(finaltexttwo)
        newim = Image.new("RGB", (int(width), int(height)))
        newim.putdata(finaltexttwo)
        newim.show()

        newim.save('temp.jpg')

        # t = time.time()

        # decrypted = int(''.join(list(map(lambda num:str(int(num)-202), ",".join([decrypted[i:i+3] for i in range(0, len(decrypted), 3)]).split(',')))))
        # decrypted = ','.join([decrypted[i:i+3] for i in range(-1, len(decrypted), 3)])

        # print(decrypted)
        # print('done at: ', time.time() - t)


        # finaltextone = [decrypted[i:i + 3] for i in range(0, len(decrypted), 3)]
        # print(finaltextone)



# encryption('akash')
decryption('akash')



    # for i in range(0, len(plaintext)):
    #     for j in range(0, 3):
    #         plaintextstr = plaintextstr + "%d" % (int(plaintext[i][j]) + 100)
    #
    # # length save for encrypted image reconstruction
    # relength = len(plaintext)
    # print(relength)
    #
    # plaintextstr += "h" + str(height) + "w" + str(width)
    # # print('--',plaintextstr)
    #
    # while (len(plaintextstr) % 16 != 0):
    #     plaintextstr = plaintextstr + "n"
    # print('')
    # print('')
    # print('')
    # print('---', plaintextstr)
