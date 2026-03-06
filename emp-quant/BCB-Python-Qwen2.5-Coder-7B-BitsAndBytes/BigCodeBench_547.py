
import hashlib
import os
import base64

def task_func(password: str, salt_length: int = 8) -> str:
    # Generate a random salt
    salt = os.urandom(salt_length)
    
    # Create a new SHA-256 hash object
    sha_signature = hashlib.sha256()
    
    # Update the hash object with the salt and password
    sha_signature.update(salt + password.encode('utf-8'))
    
    # Get the digest of the hash as bytes
    digest_bytes = sha_signature.digest()
    
    # Encode the digest in base64
    base64_encoded = base64.b64encode(digest_bytes).decode('utf-8')
    
    return base64_encoded