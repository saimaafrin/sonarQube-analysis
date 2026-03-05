
import rsa
from cryptography.fernet import Fernet
from base64 import b64encode

def task_func(file_path):
    # Generate RSA public and private keys
    public_key, private_key = rsa.newkeys(2048)

    # Read the contents of the specified file
    with open(file_path, 'r') as file:
        file_contents = file.read()

    # Generate a Fernet symmetric key
    fernet_key = Fernet.generate_key()

    # Encrypt the file contents using the Fernet key
    fernet = Fernet(fernet_key)
    encrypted_file_contents = fernet.encrypt(file_contents.encode())

    # Encrypt the Fernet key using the RSA public key
    encrypted_fernet_key = rsa.encrypt(fernet_key, public_key)

    # Save the encrypted file contents and the encrypted Fernet key in separate files
    with open('encrypted_file.txt', 'wb') as encrypted_file:
        encrypted_file.write(encrypted_file_contents)

    with open('encrypted_fernet_key.txt', 'wb') as encrypted_fernet_key_file:
        encrypted_fernet_key_file.write(encrypted_fernet_key)

    # Output the RSA public key and the filenames of the encrypted files
    print(f"PublicKey: {b64encode(public_key).decode('utf-8')}")
    print(f"Encrypted file: encrypted_file.txt")
    print(f"Encrypted Fernet key: encrypted_fernet_key.txt")