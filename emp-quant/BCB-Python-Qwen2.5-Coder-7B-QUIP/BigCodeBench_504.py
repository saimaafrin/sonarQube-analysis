
import hashlib
import rsa
import base64

def task_func(file_path):
    # Read the contents of the file
    with open(file_path, 'rb') as file:
        file_contents = file.read()

    # Hash the contents using SHA-256
    file_hash = hashlib.sha256(file_contents).digest()

    # Load the private RSA key
    with open('private.pem', 'rb') as key_file:
        private_key = rsa.PrivateKey.load_pkcs1(key_file.read())

    # Sign the hash using the private key
    signed_hash = rsa.sign(file_hash, private_key, rsa.HASH_SHA256)

    # Encode the signed hash in base64
    base64_signed_hash = base64.b64encode(signed_hash).decode('utf-8')

    return base64_signed_hash