import hashlib
import rsa
import base64
def task_func(file_path):
    # Read the file contents
    with open(file_path, 'rb') as f:
        file_contents = f.read()

    # Hash the file contents using SHA-256
    file_hash = hashlib.sha256(file_contents).hexdigest()

    # Read the private key from a file
    with open('private.pem', 'rb') as f:
        private_key = rsa.PrivateKey.load_pkcs1(f.read())

    # Sign the hash with the private key
    signed_hash = private_key.sign(file_hash.encode(), 'SHA-256')

    # Encode the signed hash in base64
    signed_hash_base64 = base64.b64encode(signed_hash)

    return signed_hash_base64