import rsa
import os
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from base64 import b64encode
def task_func(file_path):
    # Generate RSA keys
    rsa_key = rsa.generate_private_key(2048, default_backend())
    rsa_pub_key = rsa_key.public_key()

    # Encrypt file with AES
    with open(file_path, 'rb') as f:
        file_data = f.read()
    aes_key = os.urandom(32)
    aes_cipher = Cipher(algorithms.AES(aes_key), modes.CBC(aes_key), backend=default_backend())
    aes_encryptor = aes_cipher.encryptor()
    aes_encrypted_data = aes_encryptor.update(file_data) + aes_encryptor.finalize()

    # Encrypt AES key with RSA
    rsa_encryptor = rsa_key.encrypt(aes_key, padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()), algorithm=hashes.SHA256(), label=None))
    rsa_encrypted_key = rsa_encryptor.hex()

    # Save encrypted file and AES key
    with open('encrypted_file.txt', 'wb') as f:
        f.write(aes_encrypted_data)
    with open('encrypted_aes_key.txt', 'wb') as f:
        f.write(rsa_encrypted_key)

    # Return RSA public key, encrypted file name, and encrypted AES key name
    return rsa_pub_key, 'encrypted_file.txt', 'encrypted_aes_key.txt'
file_path = 'file.txt'