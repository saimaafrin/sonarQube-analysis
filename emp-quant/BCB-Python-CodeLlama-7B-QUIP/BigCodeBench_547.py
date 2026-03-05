
import hashlib
import os
import base64

def task_func(password: str, salt_length: int = 8) -> str:
    salt = os.urandom(salt_length)
    hash = hashlib.sha256(salt + password).digest()
    return base64.b64encode(hash).decode()