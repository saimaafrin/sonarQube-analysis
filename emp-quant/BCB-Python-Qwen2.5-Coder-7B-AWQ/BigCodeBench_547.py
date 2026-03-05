import hashlib
import os
import base64
def task_func(password: str, salt_length: int = 8) -> str:
    # Generate a random salt
    salt = os.urandom(salt_length)
    
    # Create a new SHA-256 hash object
    hash_object = hashlib.sha256()
    
    # Update the hash object with the salt and password
    hash_object.update(salt + password.encode('utf-8'))
    
    # Get the hexadecimal representation of the hash
    hashed_password = hash_object.hexdigest()
    
    # Encode the hashed password in base64
    base64_encoded_password = base64.b64encode(hashed_password.encode('utf-8')).decode('utf-8')
    
    return base64_encoded_password