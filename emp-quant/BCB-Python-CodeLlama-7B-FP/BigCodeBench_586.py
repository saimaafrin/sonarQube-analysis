import rsa
from cryptography.fernet import Fernet
from base64 import b64encode
def task_func(file_path):
    # Generate RSA keys
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
        backend=rsa.backends.openssl.backend
    )
    public_key = private_key.public_key()

    # Generate Fernet key
    fernet_key = Fernet.generate_key()

    # Encrypt file contents with Fernet
    with open(file_path, "rb") as file:
        file_contents = file.read()
    encrypted_file_contents = Fernet(fernet_key).encrypt(file_contents)

    # Encrypt Fernet key with RSA
    encrypted_fernet_key = public_key.encrypt(
        fernet_key,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )

    # Save encrypted file contents and Fernet key
    with open("encrypted_file_contents.txt", "wb") as file:
        file.write(encrypted_file_contents)
    with open("encrypted_fernet_key.txt", "wb") as file:
        file.write(encrypted_fernet_key)

    # Return public key and filenames
    return public_key, "encrypted_file_contents.txt", "encrypted_fernet_key.txt"