
import rsa
import os
import zipfile
from base64 import b64encode

def task_func(directory):
    # Generate RSA public and private keys
    (public_key, private_key) = rsa.newkeys(512)  # Note: 512 is too small for production; use a larger size

    # Encrypt all files in the specified directory
    encrypted_files = []
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        if os.path.isfile(file_path):
            with open(file_path, 'rb') as file:
                file_data = file.read()
                encrypted_data = rsa.encrypt(file_data, public_key)
                encrypted_files.append((filename, encrypted_data))

    # Save the encrypted files into a zip file
    zip_filename = 'encrypted_files.zip'
    with zipfile.ZipFile(zip_filename, 'w') as zip_file:
        for filename, encrypted_data in encrypted_files:
            zip_file.writestr(filename, encrypted_data)

    # Return the public key and the name of the zip file
    return public_key, zip_filename