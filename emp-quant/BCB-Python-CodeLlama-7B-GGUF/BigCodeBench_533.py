
import numpy as np
import secrets
import hashlib
import base64

def task_func(num, from_base, to_base, alphabet):
    if from_base < 2 or to_base < 2:
        raise ValueError("Invalid base for conversion")
    if not num.isdigit() or len(num) > from_base:
        raise ValueError("Invalid number format for conversion")

    salt = secrets.token_hex(16)
    num_int = int(num, from_base)
    num_bytes = num_int.to_bytes((num_int.bit_length() + 7) // 8, "big")
    hashed_bytes = hashlib.sha256(num_bytes + salt.encode()).digest()
    encoded_hash = base64.b64encode(hashed_bytes).decode()
    return encoded_hash, salt

result1, salt1 = task_func('FF', 16, 8, alphabet)
result2, salt2 = task_func('FF', 16, 8, alphabet)

print(result1 != result2)  # True