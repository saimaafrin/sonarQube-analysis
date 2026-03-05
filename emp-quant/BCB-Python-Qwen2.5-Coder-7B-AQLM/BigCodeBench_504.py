
import hashlib
import rsa
import base64

def task_func(file_path):
    # Read the contents of the file
    with open(file_path, 'rb') as file:
        file_contents = file.read()

    # Hash the file contents using SHA-256
    hash_object = hashlib.sha256(file_contents)
    file_hash = hash_object.digest()

    # Load the private RSA key
    with open('private.pem', 'rb') as key_file:
        private_key = rsa.PrivateKey.load_pkcs1(key_file.read())

    # Sign the hash with the private RSA key
    signed_hash = rsa.sign_hash(file_hash, private_key, 'SHA-256')

    # Encode the signed hash in base64
    base64_signed_hash = base64.b64encode(signed_hash).decode('utf-8')

    return base64_signed_hash