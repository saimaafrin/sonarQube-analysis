
import base64
import binascii
import os
import hashlib

def task_func(hex_str, salt_size):
    # Convert the hex string to bytes
    byte_str = binascii.unhexlify(hex_str)

    # Generate a random salt of the specified size
    salt = os.urandom(salt_size)

    # Append the salt to the byte representation of the hex string
    salted_data = byte_str + salt

    # Compute the SHA256 hash of the salted data
    hash = hashlib.sha256(salted_data).digest()

    # Return the base64-encoded salt and hash as a tuple
    return base64.b64encode(salt) + base64.b64encode(hash)