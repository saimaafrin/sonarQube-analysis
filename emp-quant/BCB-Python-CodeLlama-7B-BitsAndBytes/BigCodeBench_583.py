
import rsa
import os
from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES
from base64 import b64encode, b64decode

def task_func():
    # Generate RSA key pair
    key_pair = rsa.generate_private_key(1024)
    public_key = key_pair.publickey()

    # Encrypt private key with AES
    password = get_random_bytes(16)
    nonce = get_random_bytes(16)
    cipher = AES.new(password, AES.MODE_CBC, nonce)
    encrypted_private_key = cipher.encrypt(key_pair.exportKey('DER'))

    # Save encrypted private key to file
    filename = f"private_key_{b64encode(nonce).decode()}.txt"
    with open(filename, 'wb') as f:
        f.write(encrypted_private_key)

    # Return public key and encryption details
    return public_key, filename, password, nonce