
import numpy as np
import secrets
import hashlib
import base64

def task_func(num, from_base, to_base, alphabet):
    if from_base < 2 or to_base < 2:
        raise ValueError("Invalid base for conversion")
    if not set(num).issubset(from_base):
        raise ValueError("Invalid number format for conversion")
    salt = secrets.randbits(8)
    num_bytes = np.frombuffer(num, dtype=from_base)
    num_bytes_hashed = hashlib.sha256(num_bytes + salt).digest()
    result = base64.b64encode(num_bytes_hashed)
    return (result, salt)