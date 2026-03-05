
import base64
import hashlib
import os

def task_func(password, SALT_LENGTH=32):
    if not password:
        raise ValueError("Password cannot be None or empty")

    # Generate a random salt
    salt = os.urandom(SALT_LENGTH)

    # Hash the password using PBKDF2 with SHA-256
    hashed_password = hashlib.pbkdf2_hmac('sha256', password.encode(), salt, 100000)

    # Encode the salt and hashed password in base64
    base64_salt = base64.b64encode(salt)
    base64_hashed_password = base64.b64encode(hashed_password)

    return base64_salt, base64_hashed_password