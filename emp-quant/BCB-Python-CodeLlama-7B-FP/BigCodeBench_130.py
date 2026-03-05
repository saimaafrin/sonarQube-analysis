import base64
import binascii
import os
import hashlib
def task_func(hex_str, salt_size):
    """
    Converts a hex string to bytes, salts it with a random value of specified size, and computes its SHA256 hash.
    The function generates a random salt of the specified size, appends it to the byte representation of the hex string, and then computes the SHA256 hash of the salted data.
    The salt and hash are returned as a tuple.
    """
    # Convert hex string to bytes
    bytes_str = binascii.unhexlify(hex_str)

    # Generate a random salt of the specified size
    salt = os.urandom(salt_size)

    # Append the salt to the byte representation of the hex string
    salted_bytes = salt + bytes_str

    # Compute the SHA256 hash of the salted data
    hash = hashlib.sha256(salted_bytes).hexdigest()

    # Return the base64-encoded salt and the SHA256 hash as a tuple
    return (base64.b64encode(salt).decode(), hash)
hex_str = "0123456789abcdef"
salt_size = 16