
import binascii
import hashlib

def task_func(input_string, verify_hash=None):
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    if verify_hash is not None and not isinstance(verify_hash, str):
        raise TypeError("Verify hash must be a string or None")

    # Compute the SHA256 hash of the input string
    hash_obj = hashlib.sha256()
    hash_obj.update(input_string.encode())
    hash_bytes = hash_obj.digest()

    # Convert the hash bytes to a hexadecimal string
    hash_hex = binascii.hexlify(hash_bytes).decode()

    # Verify the computed hash against the provided hash, if provided
    if verify_hash is not None:
        if verify_hash == hash_hex:
            return hash_hex, True
        else:
            return hash_hex, False
    else:
        return hash_hex, None