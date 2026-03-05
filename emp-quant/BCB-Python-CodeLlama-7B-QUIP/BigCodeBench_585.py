
import rsa
import os
import zipfile
from base64 import b64encode

def task_func(directory):
    # Generate RSA keys
    private_key = rsa.generate_private_key(1024)
    public_key = rsa.get_public_key(private_key)

    # Encrypt all files in the specified directory
    files = os.listdir(directory)
    for file in files:
        with open(os.path.join(directory, file), 'rb') as f:
            encrypted_data = rsa.encrypt(f.read(), public_key)
            with open(os.path.join(directory, file + '.enc'), 'wb') as f:
                f.write(encrypted_data)

    # Create zip file
    zip_file = zipfile.ZipFile('encrypted_files.zip', 'w')
    for file in files:
        zip_file.write(os.path.join(directory, file + '.enc'))

    # Return public key and zip file name
    return public_key, 'encrypted_files.zip'