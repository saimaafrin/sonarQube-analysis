
import hashlib
import os
import base64

def task_func(password: str, salt_length: int = 8) -> str:
    # Generate a random salt
    salt = os.urandom(salt_length)

    # Hash the password with the salt
    hashed_password = hashlib.sha256(salt + password.encode()).hexdigest()

    # Encode the hashed password in base64
    base64_password = base64.b64encode(hashed_password.encode()).decode()

    return base64_password