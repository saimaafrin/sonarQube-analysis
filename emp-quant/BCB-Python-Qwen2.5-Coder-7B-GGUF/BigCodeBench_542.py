
import hashlib
import random
import struct

KEYS = ['470FC614', '4A0FC614', '4B9FC614', '4C8FC614', '4D7FC614']

def task_func(hex_keys=KEYS, seed=42):
    random.seed(seed)
    try:
        # Select a random hexadecimal string
        hex_key = random.choice(hex_keys)
        # Convert hexadecimal string to integer
        int_value = int(hex_key, 16)
        # Convert integer to floating-point number
        float_value = struct.unpack('!f', struct.pack('!I', int_value))[0]
        # Compute MD5 hash of the floating-point number
        md5_hash = hashlib.md5(str(float_value).encode()).hexdigest()
        return md5_hash
    except ValueError:
        raise ValueError("Invalid hexadecimal string found in the list.")