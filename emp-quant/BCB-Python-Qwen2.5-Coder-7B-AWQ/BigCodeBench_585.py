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
        # Encrypt all files in the specified directory
        for root, dirs, files in os.walk(directory):
            for file in files:
                file_path = os.path.join(root, file)
                with open(file_path, 'rb') as f:
                    file_data = f.read()
                    # Encrypt the file data using the public key
                    encrypted_data = rsa.encrypt(file_data, public_key)
                    # Add the encrypted file to the zip file
                    zipf.writestr(file, encrypted_data)

    # Return the public key and the name of the zip file
    return public_key, zip_filename