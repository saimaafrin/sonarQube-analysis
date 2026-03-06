
import binascii
import hashlib

def task_func(input_string, verify_hash=None):
    # Check if input_string is a string
    if not isinstance(input_string, str):
        raise TypeError("input_string must be a string")
    
    # Check if verify_hash is either a string or None
    if verify_hash is not None and not isinstance(verify_hash, str):
        raise TypeError("verify_hash must be a string or None")
    
    # Compute the SHA256 hash of the input string
    sha256_hash = hashlib.sha256(input_string.encode()).hexdigest()
    
    # Verify the hash if verify_hash is provided
    if verify_hash is not None:
        return sha256_hash, sha256_hash == verify_hash
    
    # Return only the computed hash if no verification is needed
    return sha256_hash