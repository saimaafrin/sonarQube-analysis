import hashlib
import rsa
import base64
def task_func(file_path):
    # Read the private key from a file
    with open('private.pem', 'rb') as f:
        private_key = f.read()

    # Hash the file contents using SHA-256
    with open(file_path, 'rb') as f:
        file_contents = f.read()
    file_hash = hashlib.sha256(file_contents).hexdigest()

    # Sign the hash with the private key
    signer = rsa.signers.PKCS1v15(rsa.PrivateKey.load_pkcs1(private_key))
    signed_hash = signer.sign(file_hash.encode())

    # Encode the signed hash in base64
    signed_hash_base64 = base64.b64encode(signed_hash)

    return signed_hash_base64