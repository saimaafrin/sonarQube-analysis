
import binascii
import hashlib

def task_func(input_string, verify_hash=None):
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    if verify_hash is not None and not isinstance(verify_hash, str):
        raise TypeError("Verify hash must be a string or None")

    hash_object = hashlib.sha256(input_string.encode())
    hex_digest = hash_object.hexdigest()

    if verify_hash is not None:
        if verify_hash == hex_digest:
            return True
        else:
            return False
    else:
        return hex_digest