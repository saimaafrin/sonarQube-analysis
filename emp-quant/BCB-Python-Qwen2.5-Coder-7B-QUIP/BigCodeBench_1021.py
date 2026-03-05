
import binascii
import hashlib
def task_func(input_string, verify_hash=None):
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    if verify_hash is not None and not isinstance(verify_hash, str):
        raise TypeError("verify_hash must be a string or None")
    
    # Compute SHA256 hash of the input string
    sha256_hash = hashlib.sha256(input_string.encode()).hexdigest()
    
    # Return the hexadecimal representation of the SHA256 hash
    return sha256_hash, (sha256_hash == verify_hash) if verify_hash is not None else None