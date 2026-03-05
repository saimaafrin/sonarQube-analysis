
import rsa
from cryptography.fernet import Fernet
from base64 import b64encode

def task_func(file_path):
    # Generate RSA keys
    private_key = rsa.generate_private_key(1024)
    public_key = rsa.get_public_key(private_key)

    # Generate Fernet key
    fernet_key = Fernet.generate_key()

    # Encrypt file contents with Fernet
    fernet_cipher = Fernet(fernet_key)
    with open(file_path, 'rb') as f:
        file_contents = f.read()
    encrypted_file_contents = fernet_cipher.encrypt(file_contents)

    # Encrypt Fernet key with RSA public key
    encrypted_fernet_key = rsa.encrypt(fernet_key, public_key)

    # Save encrypted file contents and encrypted Fernet key
    with open('encrypted_file_contents.bin', 'wb') as f:
        f.write(encrypted_file_contents)
    with open('encrypted_fernet_key.bin', 'wb') as f:
        f.write(encrypted_fernet_key)

    return public_key, 'encrypted_file_contents.bin', 'encrypted_fernet_key.bin'