
import rsa
import os
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from base64 import b64encode
def task_func(file_path):
    # Generate RSA keys
    (public_key, private_key) = rsa.newkeys(2048)
    
    # Read the file to encrypt
    with open(file_path, 'rb') as file:
        file_data = file.read()
    
    # Generate a random AES key
    aes_key = os.urandom(32)
    
    # Encrypt the file using AES
    iv = os.urandom(16)
    encryptor = Cipher(algorithms.AES(aes_key), modes.CBC(iv), backend=default_backend()).encryptor()
    encrypted_file_data = encryptor.update(file_data) + encryptor.finalize()
    
    # Encrypt the AES key using RSA
    encrypted_aes_key = rsa.encrypt(aes_key, public_key)
    
    # Save the encrypted file and the encrypted AES key
    with open('encrypted_file.bin', 'wb') as encrypted_file:
        encrypted_file.write(encrypted_file_data)
    
    with open('encrypted_aes_key.bin', 'wb') as encrypted_aes_key_file:
        encrypted_aes_key_file.write(encrypted_aes_key)
    
    # Output the RSA public key and the filenames of the encrypted files
    print(f"rsa.PublicKey: {public_key}")
    print(f"str: encrypted_file.bin")
    print(f"str: encrypted_aes_key.bin")