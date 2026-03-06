
import numpy as np
import secrets
import hashlib
import base64

def task_func(num, from_base, to_base, alphabet):
    if from_base < 2 or to_base < 2:
        raise ValueError("Invalid base for conversion")
    if not all(c in alphabet for c in num):
        raise ValueError("Invalid number format for conversion")

    # Convert the number from one base to another
    num_int = int(num, from_base)
    num_str = str(num_int)

    # Add a random salt
    salt = secrets.token_hex(16)

    # Hash the result using SHA-256
    hashed_result = hashlib.sha256(num_str.encode('utf-8') + salt.encode('utf-8')).hexdigest()

    # Encode the hash in base64 using a custom alphabet
    encoded_hash = base64.b64encode(hashed_result.encode('utf-8')).decode('utf-8')

    return encoded_hash, salt

print(result1 != result2)  # Should be True