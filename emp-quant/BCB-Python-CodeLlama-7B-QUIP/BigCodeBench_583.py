
import rsa
import os
from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES
from base64 import b64encode, b64decode

def task_func():
    # Generate RSA key pair
    private_key = rsa.generate_private_key(1024)
    public_key = rsa.get_public_key(private_key)

    # Encrypt private key with AES
    password = get_random_bytes(16)
    nonce = get_random_bytes(16)
    aes_key = AES.new(password, nonce)
    encrypted_private_key = aes_key.encrypt(private_key)

    # Save encrypted private key to file
    filename = f"private_key_{b64encode(nonce)}.txt"
    with open(filename, "wb") as f:
        f.write(b64encode(encrypted_private_key))

    return rsa.PublicKey(public_key), filename, password, nonce