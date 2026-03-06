
import rsa
import os
import zipfile
from base64 import b64encode

def task_func(directory):
    # Generate RSA public and private keys
    (public_key, private_key) = rsa.newkeys(512)

    # Create a list to store encrypted files
    encrypted_files = []

    # Encrypt each file in the specified directory
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            with open(file_path, 'rb') as f:
                file_data = f.read()
            
            # Encrypt the file data using the public key
            encrypted_data = rsa.encrypt(file_data, public_key)
            
            # Encode the encrypted data to base64 to ensure it can be stored in a text file
            encoded_data = b64encode(encrypted_data).decode('utf-8')
            
            # Save the encrypted data to a new file
            encrypted_file_path = os.path.join(root, f'{file}.enc')
            with open(encrypted_file_path, 'w') as ef:
                ef.write(encoded_data)
            
            # Add the encrypted file path to the list
            encrypted_files.append(encrypted_file_path)

    # Create a zip file containing the encrypted files
    zip_filename = 'encrypted_files.zip'
    with zipfile.ZipFile(zip_filename, 'w') as zipf:
        for encrypted_file in encrypted_files:
            zipf.write(encrypted_file, arcname=os.path.basename(encrypted_file))
    
    # Remove the original encrypted files
    for encrypted_file in encrypted_files:
        os.remove(encrypted_file)

    return public_key, zip_filename