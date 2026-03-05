
import hashlib
import random
import struct

KEYS = ['470FC614', '4A0FC614', '4B9FC614', '4C8FC614', '4D7FC614']

def task_func(hex_keys=KEYS, seed=42):
    # Set the seed for the random number generator
    random.seed(seed)

    # Select a random key from the list
    selected_key = random.choice(hex_keys)

    # Convert the selected key from hexadecimal to a floating-point number
    try:
        float_value = struct.unpack('!f', struct.pack('!I', int(selected_key, 16)))[0]
    except ValueError:
        raise ValueError("Invalid hexadecimal string")

    # Compute the MD5 hash of the floating-point number
    md5_hash = hashlib.md5(str(float_value).encode()).hexdigest()

    # Return the MD5 hash as a string
    return str(md5_hash)