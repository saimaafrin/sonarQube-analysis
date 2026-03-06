
import base64
import hashlib
import os

def task_func(password, SALT_LENGTH=32):
    if not password:
        raise ValueError("Password cannot be None or empty")
    
    # Generate a random salt
    salt = os.urandom(SALT_LENGTH)
    
    # Create a new HMAC object with SHA-256 hash function
    pbkdf2_hmac = hashlib.pbkdf2_hmac(
        'sha256',  # The hash digest algorithm for HMAC
        password.encode('utf-8'),  # Convert the password to bytes
        salt,  # The salt
        100000  # Number of iterations
    )
    
    # Encode the salt and hashed password in base64
    encoded_salt = base64.b64encode(salt)
    encoded_password = base64.b64encode(pbkdf2_hmac)
    
    return (encoded_salt, encoded_password)