from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA
import base64

CIPHERTEXT = b'YAbLcVqRe/exlpxSH0aalNqNuZ6KbddNY3ftUJG5iTzb1+3myFvQrmAaOGnENtGcjfLNopnxiJa00+qCGorRjnuZfjxLuwykArF/vepHvG4E0qndfgiPIdVk4+hzKcqJKh97qcUMUoy+/2DII+BZpHHlDRhf/EdGZ93MLXPYxukjSRCat4wo2AEYPB/0KGGm7APth6HCMu7TmuilozDRI0r93CBIWLmH3Rb7EPbAswlf9CaSDHMQTYN8PAcCajGoXWY0u2zFJ086rQKXWorWa3j+S5bWaXZ9hxBGOFZ+Zc64M4Wllle0S0q2h86oVI1BrJY4sl1DWra5ENAAIVK7DkdXujMBuEOqzxwQmt1NPNX5N3csLRMFviDt2s+YUZ2QhIU1fe+5OIc+GFE01pJtiwIYIG89j9FuTnPK/+I0dwPqUDLxAz+dz6ZH9zwBcKGut0ltnCwpOOJtZGpqONjnRZg05fdxOrL2wzvA+CVMF/1/ik5xtWXoGa2A42kMQTrFqxAOboG5erc16KJKZW4Xx+Koz1h+7NdE0dw+rj6dg+aLhpYX4o7RZqMToAsQZztvk0NFyhrYAquqhabzRC/cHHTIptOowwRFk6ewngrR3SvNEVq9jx+fzm/mhDUpYZQl4KJtM+u/bFe/GLZon+YL53U2haL1bwtd8p6H6SeplUI='

def read_private_key():
    with open("private_key.pem", "r") as file:
        key = file.read()
    return key

def read_ciphertext():
    if CIPHERTEXT:
        return CIPHERTEXT
    else:
        with open("ciphertext.txt") as file:
            ciphertext = file.read()
        return ciphertext

def decrypt(message):
    private_key = RSA.importKey(read_private_key())
    cipher = PKCS1_OAEP.new(private_key)
    plaintext = cipher.decrypt(base64.b64decode(message))
    return plaintext.decode()


if __name__ == "__main__":
    print(decrypt(read_ciphertext()))