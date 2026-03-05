
import base64
import binascii
import os
import hashlib

def task_func(hex_str, salt_size):
    # Convert hex string to bytes
    hex_bytes = binascii.unhexlify(hex_str)

    # Generate random salt
    salt = os.urandom(salt_size)

    # Append salt to hex bytes
    salted_data = salt + hex_bytes

    # Compute SHA256 hash of salted data
    hash = hashlib.sha256(salted_data).hexdigest()

    # Base64 encode salt and hash
    salt_b64 = base64.b64encode(salt).decode()
    hash_b64 = base64.b64encode(hash).decode()

    # Return tuple of base64-encoded salt and hash
    return (salt_b64, hash_b64)