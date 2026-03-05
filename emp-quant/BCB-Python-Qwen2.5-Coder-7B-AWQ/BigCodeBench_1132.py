import os
import hashlib
import base64
def task_func(password, PREFIX="ME", SALT_LENGTH=16):
    # Check if SALT_LENGTH is negative
    if SALT_LENGTH < 0:
        raise ValueError("SALT_LENGTH must be non-negative")
    
    # Generate a random salt
    salt = os.urandom(SALT_LENGTH)
    
    # Concatenate the prefix, password, and salt
    combined = PREFIX + password + salt
    
    # Hash the combined string using SHA256
    sha256_hash = hashlib.sha256(combined).digest()
    
    # Encode the hash in base64
    base64_encoded = base64.b64encode(sha256_hash).decode('utf-8')
    
    return base64_encoded