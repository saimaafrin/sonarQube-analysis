import rsa
import os
from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES
from base64 import b64encode, b64decode
def task_func():
    # Generate RSA key pair
    key_pair = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
        backend=rsa.default_backend()
    )

    # Encrypt private key with AES
    private_key = key_pair.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.TraditionalOpenSSL,
        encryption_algorithm=serialization.BestAvailableEncryption(b'password')
    )

    # Save encrypted private key to file
    filename = f'private_key_{get_random_bytes(8).hex()}.txt'
    with open(filename, 'wb') as f:
        f.write(private_key)

    # Return public key and encrypted private key filename
    return key_pair.public_key(), filename, b'password', get_random_bytes(16)