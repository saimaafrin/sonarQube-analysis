
import rsa
import os
import zipfile
from base64 import b64encode

def task_func(directory):
    # Generate RSA keys
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
        backend=rsa.default_backend()
    )
    public_key = private_key.public_key()

    # Encrypt all files in the specified directory
    encrypted_files = []
    for filename in os.listdir(directory):
        with open(os.path.join(directory, filename), 'rb') as file:
            encrypted_data = public_key.encrypt(
                file.read(),
                padding.OAEP(
                    mgf=padding.MGF1(algorithm=hashes.SHA256()),
                    algorithm=hashes.SHA256(),
                    label=None
                )
            )
        encrypted_files.append(encrypted_data)

    # Save encrypted files to a zip file
    with zipfile.ZipFile('encrypted_files.zip', 'w') as zip:
        for encrypted_file in encrypted_files:
            zip.writestr(encrypted_file, encrypted_file)

    # Return public key and zip file name
    return public_key, 'encrypted_files.zip'