
import hashlib
import rsa
import base64

def task_func(file_path):
    # Read the file contents
    with open(file_path, 'rb') as f:
        file_contents = f.read()

    # Hash the file contents with SHA-256
    hash_sha256 = hashlib.sha256(file_contents).digest()

    # Sign the hash with the private key
    signer = rsa.sign(hash_sha256, 'private.pem')

    # Encode the signed hash in base64
    signed_hash = base64.b64encode(signer)

    return signed_hash