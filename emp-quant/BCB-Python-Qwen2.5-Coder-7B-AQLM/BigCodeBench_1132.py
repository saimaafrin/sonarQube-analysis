
import os
import hashlib
import base64

def task_func(password, PREFIX="ME", SALT_LENGTH=16):
    if SALT_LENGTH < 0:
        raise ValueError("SALT_LENGTH must be non-negative")
    
    salt = os.urandom(SALT_LENGTH)
    salt_base64 = base64.b64encode(salt).decode('utf-8')
    combined_string = f"{PREFIX}{password}{salt_base64}"
    hashed_password = hashlib.sha256(combined_string.encode('utf-8')).hexdigest()
    return hashed_password