import rsa
from cryptography.fernet import Fernet
from base64 import b64encode
def task_func(file_path):
    # Generate RSA public and private keys
    (public_key, private_key) = rsa.newkeys(512)
    
    # Read the contents of the specified file
    with open(file_path, 'rb') as file:
        file_data = file.read()
    
    # Generate a Fernet symmetric key
    fernet_key = Fernet.generate_key()
    fernet = Fernet(fernet_key)
    
    # Encrypt the file contents using the Fernet key
    encrypted_file_data = fernet.encrypt(file_data)
    
    # Encrypt the Fernet key using the RSA public key
    encrypted_fernet_key = rsa.encrypt(fernet_key, public_key)
    
    # Save the encrypted file contents to a file
    encrypted_file_path = file_path + '.enc'
    with open(encrypted_file_path, 'wb') as file:
        file.write(encrypted_file_data)
    
    # Save the encrypted Fernet key to a file
    encrypted_fernet_key_path = file_path + '.key'
    with open(encrypted_fernet_key_path, 'wb') as file:
        file.write(encrypted_fernet_key)
    
    # Return the RSA public key and the paths of the encrypted files
    return b64encode(public_key.save_pkcs1()).decode(), encrypted_file_path, encrypted_fernet_key_path