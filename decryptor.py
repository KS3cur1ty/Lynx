from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA
from Crypto.Cipher import AES
import base64
import hashlib

CIPHERTEXT = b'7d+LdMWlXy/9wb/18wYMFjqq+seoR4By49NIcOmdTLEqoAKju8ceKUW11UL5pEv0eDfSNsN70INWXi2+WgC6S79V5FcFjQ2exOaMSbfz0zURerQ6P0NtYw+/FskhoC7m/f2Jh5YkQ0sRPBancsjn1n+BL/RZjDPrKG3OJAZJylLOqpfMC08TIhT/gcv1M45NvfkNE1TWLTySjMavmDvkmcKyJoCmJALCW6IbxqBM3Ie0obLsFwmqFVahil/Tb0FE'
KEY = 'h41DJF/a3Z+Plf8IUc4m98JqVkytvRZ1fxvS4Lvl10VPCYC2ZvSlAlH9ZpCw1D0F4u+cMylq9+062UCxJuIa1b2///kBYcyYqvcEWO8K1NZqkMHzhoiVlQ2xwEf6o6ySAzo+0IJ7sYVK8VdnvjUgJmfYBhFu5TyWgi5VfI3qbU8Ykbt/+IcOHR2iat7Lj8+Fsb+8GNOfs1ocq8lqLNtpaU7A5t9HDJbeZOdN50sGO/yT5jXPhnqotZaW8mZpmdz87snyZphsP30mVGJ6v0l2LIHT1x3st1tJ/NSLbl9n5tg7W6Mk1ZiZfQnRw5jMbPCijb661L7+E/H6x4q8QM8KxA+3WqTnL2xzIUH3Glfa3/9G/eeLx6dyig2V0J5K2g64E1D9CQQBv06SkIS8z7iFy+7qlGJ8Num7fvztTdi7o7lVF1cKuCkjxWPXO1LL3Hvh5026V9W1bvGPPnauH4obq5E41IUgb7Wj0XeYF92Xy3RQSrUGYXYA7TRGHxK3bWHPhAn4lAfylGP7bXbZCIWnKup7VEUljlDOLGDvPXc0s+Is9XXZLF+6UVbQA7o/cVfRp6BUgqOIzSgEL8zeBBbI9wTaLByvkhOQgfMV+OI1dq9QfhvCLZz8+Ey+2HH4PZCPXLYOh/bdLW+MMPMYpZIjLzE+vEG3EQAVAY8LmVBnbCo='



class Decrypt():
    def __init__(self):
        self.block_size = 16
        self.ciphertext = CIPHERTEXT if CIPHERTEXT else open("ciphertext.txt", "r").read()
        self.private_key = open("private_key.pem", "r").read()
        self.key = self.RSAdecrypt(KEY)

    def unpad(self, object):
        return (object[:-ord(object[len(object) - 1:])])

    def RSAdecrypt(self, key):
        private_key = RSA.importKey(self.private_key)
        cipher = PKCS1_OAEP.new(private_key)
        aes_key = cipher.decrypt(base64.b64decode(key))
        return aes_key.decode()

    def decrypt(self):
        private_key = hashlib.sha256(self.key.encode("utf-8")).digest()
        ciphertext = base64.b64decode(self.ciphertext)
        iv = ciphertext[:self.block_size]
        cipher = AES.new(private_key, AES.MODE_EAX, iv)
        return self.unpad(cipher.decrypt(ciphertext[self.block_size:]).decode("utf-8"))


if __name__ == '__main__':
    print(Decrypt().decrypt())