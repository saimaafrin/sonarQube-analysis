import rsa
import os
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from base64 import b64encode
def task_func(file_path):
    # Generate RSA keys
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
        backend=default_backend()
    )
    public_key = private_key.public_key()

    # Encrypt file with AES
    with open(file_path, 'rb') as f:
        file_data = f.read()
    aes_key = os.urandom(32)
    aes_cipher = Cipher(
        algorithms.AES(aes_key),
        modes.CBC(aes_key),
        backend=default_backend()
    )
    encryptor = aes_cipher.encryptor()
    encrypted_file_data = encryptor.update(file_data) + encryptor.finalize()

    # Encrypt AES key with RSA
    rsa_cipher = Cipher(
        algorithms.RSA(public_key),
        modes.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()),
                   algorithm=hashes.SHA256()),
        backend=default_backend()
    )
    encrypted_aes_key = rsa_cipher.encrypt(aes_key)

    # Save encrypted files
    encrypted_file_name = 'encrypted_file.bin'
    with open(encrypted_file_name, 'wb') as f:
        f.write(encrypted_file_data)
    encrypted_aes_key_name = 'encrypted_aes_key.bin'
    with open(encrypted_aes_key_name, 'wb') as f:
        f.write(encrypted_aes_key)

    # Return RSA public key and filenames
    return public_key, encrypted_file_name, encrypted_aes_key_name