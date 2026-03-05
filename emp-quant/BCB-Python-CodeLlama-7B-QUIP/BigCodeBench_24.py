
import base64
import hashlib
import os

def task_func(password, SALT_LENGTH = 32):
    if password is None or password == '':
        raise ValueError("Password cannot be empty")
    salt = os.urandom(SALT_LENGTH)
    hashed_password = hashlib.pbkdf2_hmac(password, salt, 10000, hashlib.sha256)
    return (base64.b64encode(salt), base64.b64encode(hashed_password))