import rsa
import os
from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES
from base64 import b64encode, b64decode
def task_func():
    # Generate RSA key pair
    public_key, private_key = rsa.newkeys(2048)
    
    # Generate a random filename
    random_bytes = os.urandom(8)
    filename = f"private_key_{random_bytes.hex()}.txt"
    
    # Generate a random password and nonce for AES encryption
    password = get_random_bytes(16)
    nonce = get_random_bytes(16)
    
    # Encrypt the private key with AES
    cipher = AES.new(password, AES.MODE_GCM, nonce)
    encrypted_private_key = cipher.encrypt(private_key.save_pkcs1())
    tag = cipher.tag
    
    # Save the encrypted private key to a file
    with open(filename, 'wb') as f:
        f.write(b64encode(encrypted_private_key))
        f.write(b64encode(tag))
    
    # Return the public key, filename, password, and nonce
    return public_key, filename, password, nonce