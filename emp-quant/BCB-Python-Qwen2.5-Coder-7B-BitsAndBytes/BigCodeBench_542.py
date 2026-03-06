
import hashlib
import random
import struct

KEYS = ['470FC614', '4A0FC614', '4B9FC614', '4C8FC614', '4D7FC614']

def task_func(hex_keys=KEYS, seed=42):
    # Set the seed for deterministic randomness if provided
    if seed is not None:
        random.seed(seed)

    # Select a random hexadecimal key from the list
    hex_key = random.choice(hex_keys)

    try:
        # Convert the hexadecimal string to an integer
        int_value = int(hex_key, 16)
        
        # Convert the integer to a float
        float_value = struct.unpack('!f', struct.pack('!I', int_value))[0]
        
        # Compute the MD5 hash of the float value
        md5_hash = hashlib.md5(str(float_value).encode()).hexdigest()
        
        return md5_hash
    except ValueError:
        raise ValueError("Invalid hexadecimal string encountered")