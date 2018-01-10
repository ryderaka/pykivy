# -*- coding: utf-8 -*-

from PIL import Image
from Crypto.Cipher import AES

# import random


def encryption(password):
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
            plaintext.extend(list(arr[x,y]))
            # plaintext.append(arr[x, y]) # append horizontal rgb tuples
    plaintext = str(''.join(str(x) for x in list(map(lambda x:x+202, plaintext))))

    # print(plaintext)

    plaintext+="w"+width+"w"+"h"+height+"h"

    while (len(plaintextstr) % 16 != 0):
        plaintextstr = plaintextstr + "z"

    obj = AES.new(password, AES.MODE_CBC, 'This is an IV456')
    ciphertext = obj.encrypt(plaintextstr)

    cipher_name = "cryptoimg.crypt"
    g = open(cipher_name, 'w')
    g.write(ciphertext)





    print(len(plaintext))   # image length equals to width * height

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
