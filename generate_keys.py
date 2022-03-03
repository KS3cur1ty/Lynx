#!/usr/bin/env python3
import os
from os import chmod
from Crypto import Random
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Hash import SHA

class Crypto():
    def __init__(self):
        self.private_key_path = ""
        self.public_key_path = ""
        self.bits = 4096
        self.key = None
        self.private_key_pem = None
        self.public_key_pem = None
    
    def generate_keys(self):
        self.key = RSA.generate(self.bits)
        self.private_key_pem = self.key.exportKey()
        self.public_key_pem = self.key.publickey().exportKey()

    def write_to_file(self, path):
        self.private_key_path = os.path.join(path, "private_key.pem")
        self.public_key_path = os.path.join(path, "public_key.pem")

        with open(self.private_key_path, 'w') as file:
            chmod(self.private_key_path, 600)
            file.write(self.private_key_pem.decode())
        with open(self.public_key_path, 'w') as file:
            file.write(self.public_key_pem.decode())

crypto = Crypto()
crypto.generate_keys()
crypto.write_to_file(".")