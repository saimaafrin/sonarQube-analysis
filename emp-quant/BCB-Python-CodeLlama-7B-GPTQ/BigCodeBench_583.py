import rsa
import os
from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES
from base64 import b64encode, b64decode
def task_func():
    # Generate RSA key pair
    key_pair = rsa.newkeys(1024)
    public_key = key_pair.publickey()

    # Generate encryption password and nonce
    password = get_random_bytes(16)
    nonce = get_random_bytes(16)

    # Encrypt private key with AES
    private_key = key_pair.privatekey()
    cipher = AES.new(password, AES.MODE_GCM, nonce=nonce)
    encrypted_private_key = cipher.encrypt(private_key.exportKey())

    # Save encrypted private key to file
    filename = f"private_key_{b64encode(nonce).decode()}.txt"
    with open(filename, "wb") as f:
        f.write(encrypted_private_key)

    # Return public key, filename, encryption password, and nonce
    return public_key, filename, password, nonce
cipher = AES.new(password, AES.MODE_GCM, nonce=nonce)