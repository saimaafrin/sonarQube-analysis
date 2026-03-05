import base64
import hashlib
import os
from Crypto.Protocol.KDF import PBKDF2
def task_func(password, SALT_LENGTH = 32):
    if password is None or password == "":
        raise ValueError("Password cannot be None or empty")
    
    # Generate a random salt
    salt = os.urandom(SALT_LENGTH)
    
    # Hash the password using PBKDF2 with SHA-256
    hashed_password = PBKDF2(password, salt, dkLen=32, count=100000, prf=hashlib.sha256)
    
    # Encode the salt and hashed password in base64
    salt_base64 = base64.b64encode(salt)
    hashed_password_base64 = base64.b64encode(hashed_password)
    
    return (salt_base64, hashed_password_base64)