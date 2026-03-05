import base64
import hashlib
import os
def task_func(password, SALT_LENGTH = 32):
    if password is None or password == "":
        raise ValueError("Password cannot be None or empty")
    
    # Generate a random salt
    salt = os.urandom(SALT_LENGTH)
    
    # Create a new HMAC object using SHA-256
    hmac_obj = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)
    
    # Encode the salt and the hashed password in base64
    salt_base64 = base64.b64encode(salt)
    hashed_password_base64 = base64.b64encode(hmac_obj)
    
    return (salt_base64, hashed_password_base64)