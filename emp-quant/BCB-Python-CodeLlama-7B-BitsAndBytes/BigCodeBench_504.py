
import hashlib
import rsa
import base64

def task_func(file_path):
    # Read the file contents
    with open(file_path, 'rb') as f:
        file_contents = f.read()

    # Hash the file contents using SHA-256
    hash_object = hashlib.sha256(file_contents)
    hash_value = hash_object.hexdigest()

    # Sign the hash value with the private key
    with open('private.pem', 'rb') as f:
        private_key = rsa.PrivateKey.load_pkcs1(f.read())
        signature = rsa.sign(hash_value, private_key, 'SHA-256')

    # Encode the signature in base64
    signature_b64 = base64.b64encode(signature)

    return signature_b64