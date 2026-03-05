import base64
import binascii
import os
import hashlib
def task_func(hex_str, salt_size):
    # Convert hex string to bytes
    byte_data = binascii.unhexlify(hex_str)
    
    # Generate a random salt of the specified size
    salt = os.urandom(salt_size)
    
    # Append the salt to the byte representation of the hex string
    salted_data = byte_data + salt
    
    # Compute the SHA256 hash of the salted data
    sha256_hash = hashlib.sha256(salted_data).digest()
    
    # Encode the salt in base64
    base64_salt = base64.b64encode(salt).decode('utf-8')
    
    # Return the base64-encoded salt and the SHA256 hash as a tuple
    return (base64_salt, sha256_hash)