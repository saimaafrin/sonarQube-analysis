import rsa
from cryptography.fernet import Fernet
from base64 import b64encode
def task_func(file_path):
    # Generate RSA public and private keys
    (public_key, private_key) = rsa.newkeys(512)
    
    # Read the contents of the specified file
    with open(file_path, 'rb') as file:
        file_data = file.read()
    
    # Encrypt the file contents using Fernet symmetric encryption
    fernet = Fernet(Fernet.generate_key())
    encrypted_data = fernet.encrypt(file_data)
    
    # Encrypt the Fernet key with the RSA public key
    encrypted_fernet_key = rsa.encrypt(fernet.key, public_key)
    
    # Save the encrypted file contents and the encrypted Fernet key in separate files
    encrypted_file_path = file_path + '.enc'
    with open(encrypted_file_path, 'wb') as file:
        file.write(encrypted_data)
    
    encrypted_fernet_key_path = file_path + '.fernet.enc'
    with open(encrypted_fernet_key_path, 'wb') as file:
        file.write(encrypted_fernet_key)
    
    # Return the RSA public key and the filenames of the encrypted files
    return b64encode(public_key).decode('utf-8'), encrypted_file_path, encrypted_fernet_key_path