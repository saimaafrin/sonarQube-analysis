import rsa
import os
import zipfile
from base64 import b64encode
def task_func(directory):
    # Generate RSA keys
    rsa_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
        backend=rsa.backends.openssl.backend
    )
    public_key = rsa_key.public_key()

    # Encrypt all files in the specified directory
    files = os.listdir(directory)
    encrypted_files = []
    for file in files:
        with open(os.path.join(directory, file), 'rb') as f:
            encrypted_data = rsa.encrypt(f.read(), public_key)
        encrypted_files.append(encrypted_data)

    # Save encrypted files to a zip file
    zip_file = zipfile.ZipFile(f'{directory}.zip', 'w')
    for encrypted_file in encrypted_files:
        zip_file.writestr(encrypted_file, encrypted_file)
    zip_file.close()

    # Return public key and zip file name
    return public_key, f'{directory}.zip'
directory = 'test_files'