
import base64
import binascii
import os
import hashlib

def task_func(hex_str, salt_size):
    # Convert hex string to bytes
    try:
        byte_data = binascii.unhexlify(hex_str)
    except binascii.Error:
        raise ValueError("Invalid hex string")

    # Generate a random salt of the specified size
    salt = os.urandom(salt_size)

    # Append the salt to the byte representation of the hex string
    salted_data = byte_data + salt

    # Compute the SHA256 hash of the salted data
    sha256_hash = hashlib.sha256(salted_data).digest()

    # Encode the salt and hash in base64
    salt_base64 = base64.b64encode(salt).decode('utf-8')
    hash_base64 = base64.b64encode(sha256_hash).decode('utf-8')

    return (salt_base64, hash_base64)