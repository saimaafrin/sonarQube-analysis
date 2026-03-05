import base64
import binascii
import os
import hashlib
def task_func(hex_str, salt_size):
    # Convert hex string to bytes
    hex_bytes = binascii.unhexlify(hex_str)

    # Generate a random salt of the given size
    salt = os.urandom(salt_size)

    # Append the salt to the byte representation of the hex string
    salted_data = salt + hex_bytes

    # Compute the SHA256 hash of the salted data
    hash = hashlib.sha256(salted_data).hexdigest()

    # Return the base64-encoded salt and the SHA256 hash as a tuple
    return (base64.b64encode(salt).decode(), hash)
hex_str = "0123456789abcdef"
salt_size = 16