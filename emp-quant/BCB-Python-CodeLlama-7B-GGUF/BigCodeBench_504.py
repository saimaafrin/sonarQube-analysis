
import hashlib
import rsa
import base64

def task_func(file_path):
    # Read the file contents
    with open(file_path, 'rb') as f:
        file_contents = f.read()

    # Hash the file contents using SHA-256
    hash = hashlib.sha256(file_contents).hexdigest()

    # Load the private key from the file
    with open('private.pem', 'rb') as f:
        private_key = rsa.PrivateKey.load_pkcs1(f.read())

    # Sign the hash with the private key
    signature = private_key.sign(hash.encode(), 'SHA-256')

    # Encode the signature in base64
    base64_signature = base64.b64encode(signature)

    # Return the base64 encoded signed hash
    return base64_signature