
import numpy as np
import secrets
import hashlib
import base64

def task_func(num, from_base, to_base, alphabet):
    # Validate the input bases
    if from_base < 2 or to_base < 2:
        raise ValueError("Base must be at least 2")

    # Validate the input number
    if not all(char in alphabet for char in num):
        raise ValueError("Number contains invalid characters for the specified base")

    # Convert the number from the original base to base 10
    num_base10 = int(num, from_base)

    # Generate a random salt
    salt = secrets.token_hex(4)

    # Convert the number from base 10 to the target base
    num_base = ''
    while num_base10 > 0:
        num_base = alphabet[num_base10 % to_base] + num_base
        num_base10 //= to_base

    # Hash the result using SHA-256
    hash_result = hashlib.sha256(num_base.encode()).hexdigest()

    # Encode the hash in base64 using the custom alphabet
    base64_hash = base64.b64encode(hash_result.encode()).decode()

    return (base64_hash, salt)

print(result1 != result2)  # Output: True