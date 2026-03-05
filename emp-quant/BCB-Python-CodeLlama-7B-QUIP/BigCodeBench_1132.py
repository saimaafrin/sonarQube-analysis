
import os
import hashlib
import base64

def task_func(password, PREFIX="ME", SALT_LENGTH=16):
    if SALT_LENGTH < 0:
        raise ValueError("SALT_LENGTH must be non-negative")
    salt = os.urandom(SALT_LENGTH)
    hashed_password = hashlib.sha256(salt + PREFIX + password).digest()
    return base64.b64encode(hashed_password)