
import rsa
from cryptography.fernet import Fernet
from base64 import b64encode

def task_func(file_path):
    # Generate RSA keys
    private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
    public_key = private_key.public_key()

    # Encrypt file contents with Fernet
    with open(file_path, 'rb') as f:
        file_contents = f.read()
    fernet = Fernet(Fernet.generate_key())
    encrypted_file_contents = fernet.encrypt(file_contents)

    # Encrypt Fernet key with RSA public key
    encrypted_fernet_key = public_key.encrypt(fernet.key, padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()), algorithm=hashes.SHA256(), label=None))

    # Save encrypted file contents and Fernet key to separate files
    with open('encrypted_file_contents.txt', 'wb') as f:
        f.write(encrypted_file_contents)
    with open('encrypted_fernet_key.txt', 'wb') as f:
        f.write(encrypted_fernet_key)

    # Print public key and filenames
    print('PublicKey:', public_key.export_key())
    print('Encrypted file:', 'encrypted_file_contents.txt')
    print('Encrypted Fernet key:', 'encrypted_fernet_key.txt')