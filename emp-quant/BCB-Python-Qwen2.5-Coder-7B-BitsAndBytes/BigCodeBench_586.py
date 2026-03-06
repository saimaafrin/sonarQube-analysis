
import rsa
from cryptography.fernet import Fernet
from base64 import b64encode

def task_func(file_path):
    # Generate RSA public and private keys
    (public_key, private_key) = rsa.newkeys(512)
    
    # Encrypt the contents of the specified file using Fernet symmetric encryption
    fernet = Fernet.generate_key()
    cipher_suite = Fernet(fernet)
    with open(file_path, 'rb') as file:
        file_data = file.read()
    encrypted_file_data = cipher_suite.encrypt(file_data)
    
    # Save the encrypted file contents to a new file
    encrypted_file_path = file_path + '.enc'
    with open(encrypted_file_path, 'wb') as file:
        file.write(encrypted_file_data)
    
    # Encrypt the Fernet key with the RSA public key
    rsa_public_key = rsa.PublicKey.load_pkcs1(public_key)
    encrypted_fernet_key = rsa.encrypt(fernet, rsa_public_key)
    
    # Save the encrypted Fernet key to a new file
    encrypted_fernet_key_path = file_path + '_key.enc'
    with open(encrypted_fernet_key_path, 'wb') as file:
        file.write(encrypted_fernet_key)
    
    # Return the RSA public key and the paths of the encrypted files
    return {
        "PublicKey": b64encode(public_key).decode('utf-8'),
        "EncryptedFile": encrypted_file_path,
        "EncryptedFernetKey": encrypted_fernet_key_path
    }