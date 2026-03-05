
import hashlib
import os
import base64

def task_func(password: str, salt_length: int = 8) -> str:
    # Generate a random salt
    salt = os.urandom(salt_length)
    
    # Create a new SHA-256 hash object
    hash_obj = hashlib.sha256()
    
    # Update the hash object with the salt and password
    hash_obj.update(salt + password.encode())
    
    # Get the hexadecimal representation of the hash
    hex_digest = hash_obj.hexdigest()
    
    # Encode the hexadecimal digest in base64
    base64_bytes = base64.b64encode(hex_digest.encode())
    
    # Return the base64 encoded string
    return base64_bytes.decode()