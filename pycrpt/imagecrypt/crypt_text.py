# -*- coding: utf-8 -*-

from Crypto.Cipher import AES
import hashlib


def encryption(password, input_text):
    password = hashlib.sha256(password.encode('utf-8')).digest()

    encryption_suite = AES.new(password, AES.MODE_CBC, 'This is an IV456')
    while len(input_text) % 16 != 0:
        input_text += ' '
    cipher_text = encryption_suite.encrypt(input_text)
    return cipher_text


def decryption(password, input_text):
    password = hashlib.sha256(password.encode('utf-8')).digest()

    encryption_suite = AES.new(password, AES.MODE_CBC, 'This is an IV456')
    cipher_text = encryption_suite.encrypt(input_text)
    return cipher_text.strip()
