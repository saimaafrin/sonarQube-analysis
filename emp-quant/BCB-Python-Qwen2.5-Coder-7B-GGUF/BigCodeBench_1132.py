
import os
import hashlib
import base64

def task_func(password, PREFIX="ME", SALT_LENGTH=16):
    if SALT_LENGTH < 0:
        raise ValueError("SALT_LENGTH must be non-negative")
    
    salt = os.urandom(SALT_LENGTH)
    salted_password = PREFIX + password + salt
    hashed_password = hashlib.sha256(salted_password).digest()
    base64_encoded = base64.b64encode(hashed_password).decode('utf-8')
    
    return base64_encoded