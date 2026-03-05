import rsa
import os
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from base64 import b64encode
def task_func(file_path):
    # Generate RSA public and private keys
    (public_key, private_key) = rsa.newkeys(512)

    # Read the file to be encrypted
    with open(file_path, 'rb') as file:
        file_data = file.read()

    # Encrypt the file using AES encryption
    aes_key = os.urandom(32)  # AES-256 key
    iv = os.urandom(16)  # AES block size
    cipher = Cipher(algorithms.AES(aes_key), modes.CFB(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    padded_data = padding.PKCS7(algorithms.AES.block_size).padder().update(file_data) + padding.PKCS7(algorithms.AES.block_size).padder().finalize()
    encrypted_file_data = encryptor.update(padded_data) + encryptor.finalize()

    # Encrypt the AES key with the RSA public key
    encrypted_aes_key = rsa.encrypt(aes_key, public_key)

    # Save the encrypted file and the encrypted AES key in separate new files
    encrypted_file_path = file_path + '.enc'
    with open(encrypted_file_path, 'wb') as file:
        file.write(encrypted_file_data)

    encrypted_aes_key_path = file_path + '.aes.enc'
    with open(encrypted_aes_key_path, 'wb') as file:
        file.write(encrypted_aes_key)

    return public_key, encrypted_file_path, encrypted_aes_key_path