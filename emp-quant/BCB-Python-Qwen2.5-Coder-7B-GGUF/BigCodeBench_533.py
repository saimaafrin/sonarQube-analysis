
import numpy as np
import secrets
import hashlib
import base64

def task_func(num, from_base, to_base, alphabet):
    # Validate the base values
    if from_base < 2 or to_base < 2:
        raise ValueError("Base values must be at least 2")
    
    # Validate the number format
    valid_chars = set(alphabet[:from_base])
    if not set(num).issubset(valid_chars):
        raise ValueError("Number contains invalid characters for the specified base")
    
    # Convert the number from the original base to base 10
    num_base10 = int(num, from_base)
    
    # Add a random salt
    salt = secrets.token_hex(4)
    salted_num = num_base10 + int(salt, 16)
    
    # Hash the salted number using SHA-256
    hash_object = hashlib.sha256(str(salted_num).encode())
    hash_hex = hash_object.hexdigest()
    
    # Encode the hash in base64 using the custom alphabet
    hash_bytes = hash_hex.encode()
    hash_base64 = base64.b64encode(hash_bytes).decode()
    hash_base64 = ''.join([alphabet.index(c) for c in hash_base64])
    
    return hash_base64, salt