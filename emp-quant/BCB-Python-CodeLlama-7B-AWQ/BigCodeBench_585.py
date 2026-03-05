import rsa
import os
import zipfile
from base64 import b64encode
def task_func(directory):
    # Generate RSA keys
    rsa_keys = rsa.generate_keys(2048)
    public_key = rsa_keys.publickey
    private_key = rsa_keys.privatekey

    # Encrypt all files in the specified directory using the public key
    encrypted_files = []
    for filename in os.listdir(directory):
        with open(os.path.join(directory, filename), 'rb') as file:
            encrypted_data = public_key.encrypt(file.read(), 32)
            encrypted_files.append((filename, encrypted_data))

    # Save the encrypted files into a zip file
    zip_filename = 'encrypted_files.zip'
    with zipfile.ZipFile(zip_filename, 'w') as zip_file:
        for filename, encrypted_data in encrypted_files:
            zip_file.writestr(filename, encrypted_data)

    # Return the public key and the name of the zip file
    return public_key, zip_filename
directory = 'files'