
import numpy as np
import secrets
import hashlib
import base64

def task_func(num, from_base, to_base, alphabet):
    if from_base < 2 or to_base < 2:
        raise ValueError("Base must be at least 2")
    
    try:
        num_int = int(num, from_base)
    except ValueError:
        raise ValueError(f"Invalid number format for base {from_base}")
    
    salt = secrets.token_hex(16)
    combined = str(num_int) + salt
    
    sha256_hash = hashlib.sha256(combined.encode()).digest()
    
    encoded_hash = base64.b64encode(sha256_hash).decode()
    
    # Custom encoding
    encoded_result = ''.join(alphabet[ord(c) % len(alphabet)] for c in encoded_hash)
    
    return (encoded_result, salt)

print(result1 != result2)  # Should print True