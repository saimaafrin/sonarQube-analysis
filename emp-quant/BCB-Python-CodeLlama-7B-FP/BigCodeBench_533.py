import numpy as np
import secrets
import hashlib
import base64
def task_func(num, from_base, to_base, alphabet):
    """
    Converts a number from one base to another, adds a random salt, hashes the result using SHA-256, and then encodes the hash in base64 using a custom alphabet.
    The function also returns the used salt. Verify that different invocations produce different results due to the random salt.
    """
    if from_base < 2 or to_base < 2:
        raise ValueError("Invalid base for conversion")
    if not num.isdigit():
        raise ValueError("Invalid number format")

    # Convert the number from the specified base to decimal
    num_decimal = int(num, from_base)

    # Add a random salt to the number
    salt = secrets.token_hex(16)
    num_decimal += int(salt, 16)

    # Hash the number using SHA-256
    hash = hashlib.sha256(str(num_decimal).encode()).hexdigest()

    # Encode the hash in base64 using a custom alphabet
    encoded_hash = base64.b64encode(hash.encode()).decode()

    # Return the encoded hash and the used salt
    return encoded_hash, salt