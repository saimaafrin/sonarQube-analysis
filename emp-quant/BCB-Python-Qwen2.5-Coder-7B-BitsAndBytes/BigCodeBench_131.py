
import base64
import binascii
import os
import hashlib

def task_func(hex_str, salt_size):
    # Convert hex string to bytes
    byte_data = binascii.unhexlify(hex_str)
    
    # Generate a random salt of the specified size
    salt = os.urandom(salt_size)
    
    # Append the salt to the byte data
    salted_data = byte_data + salt
    
    # Compute the SHA256 hash of the salted data
    sha256_hash = hashlib.sha256(salted_data).digest()
    
    # Encode the salt and hash in base64
    encoded_salt = base64.b64encode(salt).decode('utf-8')
    encoded_hash = base64.b64encode(sha256_hash).decode('utf-8')
    
    return (encoded_salt, encoded_hash)