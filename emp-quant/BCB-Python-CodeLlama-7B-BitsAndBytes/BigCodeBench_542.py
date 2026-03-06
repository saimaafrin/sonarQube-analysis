
import hashlib
import random
import struct

KEYS = ['470FC614', '4A0FC614', '4B9FC614', '4C8FC614', '4D7FC614']

def task_func(hex_keys=KEYS, seed=42):
    # Check if the input is a list of hexadecimal strings
    if not all(all(c in '0123456789ABCDEF' for c in key) for key in hex_keys):
        raise ValueError('Invalid hexadecimal string')

    # Select a random key from the list
    random.seed(seed)
    selected_key = random.choice(hex_keys)

    # Convert the selected key to a floating-point number
    float_value = struct.unpack('f', bytes.fromhex(selected_key))[0]

    # Compute the MD5 hash of the floating-point number
    md5_hash = hashlib.md5(struct.pack('f', float_value)).hexdigest()

    # Return the MD5 hash
    return md5_hash