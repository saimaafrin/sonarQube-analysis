
import rsa
import os
from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES
from base64 import b64encode, b64decode

def task_func():
    # Generate RSA key pair
    key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
        backend=rsa.backends.openssl_backend()
    )

    # Encrypt private key with AES
    password = get_random_bytes(16)
    nonce = get_random_bytes(16)
    cipher = AES.new(password, AES.MODE_GCM, nonce)
    encrypted_key = cipher.encrypt(key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.TraditionalOpenSSL,
        encryption_algorithm=serialization.BestAvailableEncryption(password)
    ))

    # Save encrypted private key to file
    filename = f"private_key_{b64encode(get_random_bytes(8)).decode()}.txt"
    with open(filename, "wb") as f:
        f.write(encrypted_key)

    # Return public key, filename, encryption password, and nonce
    return key.public_key(), filename, password, nonce