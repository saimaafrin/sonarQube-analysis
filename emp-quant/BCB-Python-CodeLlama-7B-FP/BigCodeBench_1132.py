import os
import hashlib
import base64
def task_func(password, PREFIX="ME", SALT_LENGTH=16):
    """
    Generates a hashed password by concatenating a given password with a generated salt, and then hashing the combined string using SHA256.
    The hashed result is then encoded in base64.
    """
    if SALT_LENGTH < 0:
        raise ValueError("SALT_LENGTH must be non-negative")

    salt = os.urandom(SALT_LENGTH)
    hashed_password = hashlib.sha256(f"{PREFIX}{salt}{password}".encode()).hexdigest()
    return base64.b64encode(hashed_password.encode()).decode()