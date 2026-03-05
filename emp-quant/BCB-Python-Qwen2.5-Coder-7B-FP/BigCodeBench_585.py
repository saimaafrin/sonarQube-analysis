import rsa
import os
import zipfile
from base64 import b64encode
def task_func(directory):
    # Generate RSA public and private keys
    (public_key, private_key) = rsa.newkeys(512)

    # Create a zip file to store encrypted files
    zip_filename = 'encrypted_files.zip'
    with zipfile.ZipFile(zip_filename, 'w') as zipf:
        # Encrypt each file in the specified directory
        for filename in os.listdir(directory):
            file_path = os.path.join(directory, filename)
            if os.path.isfile(file_path):
                with open(file_path, 'rb') as file:
                    file_data = file.read()
                    # Encrypt the file data using the public key
                    encrypted_data = rsa.encrypt(file_data, public_key)
                    # Store the encrypted data in the zip file
                    zipf.writestr(filename, encrypted_data)

    return public_key, zip_filename