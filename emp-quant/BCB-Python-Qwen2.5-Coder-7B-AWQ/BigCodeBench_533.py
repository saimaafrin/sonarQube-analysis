import numpy as np
import secrets
import hashlib
import base64
def task_func(num, from_base, to_base, alphabet):
    # Validate input bases
    if from_base < 2 or to_base < 2:
        raise ValueError("Base must be at least 2")
    
    # Validate number format
    valid_chars = set(alphabet[:from_base])
    if not all(char in valid_chars for char in num):
        raise ValueError("Number contains invalid characters for the specified base")
    
    # Convert number from from_base to 10
    decimal_num = int(num, from_base)
    
    # Convert number from 10 to to_base
    converted_num = np.base_repr(decimal_num, to_base)
    
    # Generate a random salt
    salt = secrets.token_hex(4)
    
    # Hash the converted number with the salt
    hash_object = hashlib.sha256((converted_num + salt).encode())
    hash_result = hash_object.hexdigest()
    
    # Encode the hash in base64 using the custom alphabet
    base64_encoded = base64.b64encode(hash_result.encode()).decode()
    base64_encoded = ''.join(alphabet[alphabet.index(char)] for char in base64_encoded)
    
    return base64_encoded, salt
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"