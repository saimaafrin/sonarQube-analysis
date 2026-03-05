import hashlib
import os
import base64
def task_func(password: str, salt_length: int = 8) -> str:
    """
    Encrypt a password using Salt and SHA-256, then encode the result in base64.
    """
    salt = os.urandom(salt_length)
    hashed_password = hashlib.sha256(password.encode('utf-8') + salt).hexdigest()
    return base64.b64encode(hashed_password.encode('utf-8')).decode('utf-8')