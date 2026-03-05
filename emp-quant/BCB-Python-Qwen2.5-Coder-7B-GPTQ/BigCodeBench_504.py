import hashlib
import rsa
import base64
def task_func(file_path):
    # Read the file content
    with open(file_path, 'rb') as file:
        file_content = file.read()
    
    # Hash the file content using SHA-256
    file_hash = hashlib.sha256(file_content).digest()
    
    # Load the private RSA key
    with open('private.pem', 'rb') as key_file:
        private_key = rsa.PrivateKey.load_pkcs1(key_file.read())
    
    # Sign the hash with the private RSA key
    signed_hash = rsa.sign_hash(file_hash, private_key, 'SHA-256')
    
    # Encode the signed hash in base64
    base64_signed_hash = base64.b64encode(signed_hash).decode('utf-8')
    
    return base64_signed_hash