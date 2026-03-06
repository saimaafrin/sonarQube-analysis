
import rsa
import os
from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES
from base64 import b64encode, b64decode

def task_func():
    # Generate RSA key pair
    (public_key, private_key) = rsa.newkeys(2048)
    
    # Generate random bytes for the filename
    filename_hex = ''.join([format(os.urandom(1)[0], '02x') for _ in range(8)])
    filename = f"private_key_{filename_hex}.txt"
    
    # Generate encryption password and nonce
    password = get_random_bytes(32)
    nonce = get_random_bytes(16)
    
    # Encrypt the private key using AES
    cipher = AES.new(password, AES.MODE_GCM, nonce=nonce)
    encrypted_private_key = cipher.encrypt(rsa.key.export_key(private_key))
    
    # Save the encrypted private key to a file
    with open(filename, 'wb') as f:
        f.write(b64encode(nonce + cipher.nonce + cipher.tag + encrypted_private_key))
    
    return public_key, filename, password, nonce