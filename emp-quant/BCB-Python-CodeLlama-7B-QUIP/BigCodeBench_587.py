
import rsa
import os
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from base64 import b64encode

def task_func(file_path):
    # Generate RSA keys
    private_key = rsa.generate_private_key(1024)
    public_key = rsa.get_public_key(private_key)

    # Encrypt the file with AES
    aes_key = os.urandom(32)
    aes_cipher = Cipher(algorithms.AES(aes_key), modes.CBC(aes_key), default_backend())
    with open(file_path, 'rb') as f:
        file_content = f.read()
    aes_ciphertext = aes_cipher.encrypt(file_content)

    # Encrypt the AES key with the RSA public key
    rsa_cipher = Cipher(algorithms.RSA(public_key), modes.CBC(aes_key), default_backend())
    rsa_ciphertext = rsa_cipher.encrypt(aes_key)

    # Save the encrypted file and the encrypted AES key
    with open('encrypted_file', 'wb') as f:
        f.write(rsa_ciphertext)
    with open('encrypted_aes_key', 'wb') as f:
        f.write(aes_ciphertext)

    return rsa_ciphertext, aes_ciphertext