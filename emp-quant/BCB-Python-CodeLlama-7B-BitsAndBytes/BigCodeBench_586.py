
import rsa
from cryptography.fernet import Fernet
from base64 import b64encode

def task_func(file_path):
    # Generate RSA keys
    private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
    public_key = private_key.public_key()

    # Encrypt file contents with Fernet
    with open(file_path, 'rb') as file:
        file_contents = file.read()
    fernet = Fernet(b64encode(file_contents))
    encrypted_file_contents = fernet.encrypt(file_contents)

    # Encrypt Fernet key with RSA
    encrypted_fernet_key = public_key.encrypt(fernet.key, 32)

    # Save encrypted file contents and encrypted Fernet key to separate files
    with open('encrypted_file_contents.txt', 'wb') as file:
        file.write(encrypted_file_contents)
    with open('encrypted_fernet_key.txt', 'wb') as file:
        file.write(encrypted_fernet_key)

    # Output public key and filenames
    print('PublicKey:', public_key.export_key('PEM'))
    print('Encrypted file:', 'encrypted_file_contents.txt')
    print('Encrypted Fernet key:', 'encrypted_fernet_key.txt')

# Call the function with the file path as an argument
task_func('example_file.txt')