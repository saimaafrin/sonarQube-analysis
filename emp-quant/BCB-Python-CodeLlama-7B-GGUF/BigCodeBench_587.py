
import rsa
import os
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from base64 import b64encode

def task_func(file_path):
    # Generate RSA keys
    private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048, backend=default_backend())
    public_key = private_key.public_key()

    # Encrypt file with AES
    with open(file_path, 'rb') as f:
        file_data = f.read()
    aes_key = os.urandom(32)
    aes_cipher = Cipher(algorithms.AES(aes_key), modes.CBC(aes_key), backend=default_backend())
    aes_encryptor = aes_cipher.encryptor()
    aes_encrypted_data = aes_encryptor.update(file_data) + aes_encryptor.finalize()

    # Encrypt AES key with RSA
    rsa_cipher = Cipher(algorithms.RSA(public_key), modes.PKCS1v15(), backend=default_backend())
    rsa_encryptor = rsa_cipher.encryptor()
    rsa_encrypted_aes_key = rsa_encryptor.update(aes_key) + rsa_encryptor.finalize()

    # Save encrypted file and AES key
    with open('encrypted_file.txt', 'wb') as f:
        f.write(aes_encrypted_data)
    with open('encrypted_aes_key.txt', 'wb') as f:
        f.write(rsa_encrypted_aes_key)

    # Return RSA public key and filenames
    return public_key, 'encrypted_file.txt', 'encrypted_aes_key.txt'

# Call the function with the path to the file to be encrypted
public_key, encrypted_file, encrypted_aes_key = task_func('path/to/file.txt')

# Print the RSA public key and filenames
print(public_key)
print(encrypted_file)
print(encrypted_aes_key)