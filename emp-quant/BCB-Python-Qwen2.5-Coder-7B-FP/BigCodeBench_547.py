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
    
    # Get the hexadecimal representation of the digest
    hex_digest = hash_object.hexdigest()
    
    # Encode the hexadecimal digest in base64
    base64_encoded = base64.b64encode(hex_digest.encode('utf-8')).decode('utf-8')
    
    # Return the base64 encoded string
    return base64_encoded