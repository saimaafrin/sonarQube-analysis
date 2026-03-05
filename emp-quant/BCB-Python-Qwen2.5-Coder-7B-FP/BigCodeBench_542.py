import hashlib
import random
import struct
KEYS = ['470FC614', '4A0FC614', '4B9FC614', '4C8FC614', '4D7FC614']
def task_func(hex_keys=KEYS, seed=42):
    # Set the seed for random number generation for deterministic results
    random.seed(seed)
    
    # Select a random hexadecimal string from the list
    selected_hex = random.choice(hex_keys)
    
    # Validate the selected hexadecimal string
    try:
        # Convert the hexadecimal string to an integer
        hex_int = int(selected_hex, 16)
    except ValueError:
        raise ValueError("Invalid hexadecimal string")
    
    # Convert the integer to a floating-point number
    float_num = struct.unpack('!f', struct.pack('!I', hex_int))[0]
    
    # Compute the MD5 hash of the floating-point number
    md5_hash = hashlib.md5(str(float_num).encode()).hexdigest()
    
    # Return the MD5 hash as a string
    return md5_hash