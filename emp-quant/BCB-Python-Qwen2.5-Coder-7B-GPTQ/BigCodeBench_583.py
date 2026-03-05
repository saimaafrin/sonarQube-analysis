import rsa
import os
from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES
from base64 import b64encode, b64decode
def task_func():
    # Generate RSA key pair
    public_key, private_key = rsa.newkeys(2048)
    
    # Generate a random password for AES encryption
    password = get_random_bytes(16)
    
    # Generate a random nonce for AES encryption
    nonce = get_random_bytes(16)
    
    # Encrypt the private key using AES
    cipher = AES.new(password, AES.MODE_GCM, nonce)
    encrypted_private_key = cipher.encrypt(private_key.save_pkcs1())
    
    # Generate a filename for the encrypted private key
    filename = f"private_key_{os.urandom(8).hex()}.txt"
    
    # Save the encrypted private key to a file
    with open(filename, 'wb') as f:
        f.write(encrypted_private_key)
    
    # Return the RSA public key, filename, password, and nonce
    return public_key, filename, password, nonce