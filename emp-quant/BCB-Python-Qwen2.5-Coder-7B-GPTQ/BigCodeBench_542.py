import hashlib
import random
import struct
KEYS = ['470FC614', '4A0FC614', '4B9FC614', '4C8FC614', '4D7FC614']
def task_func(hex_keys=KEYS, seed=42):
    # Set the seed for deterministic random choices
    random.seed(seed)
    
    # Select a random hexadecimal string from the list
    selected_hex = random.choice(hex_keys)
    
    # Convert the hexadecimal string to a floating-point number
    try:
        float_number = struct.unpack('!f', bytes.fromhex(selected_hex))[0]
    except struct.error:
        raise ValueError("Invalid hexadecimal string")
    
    # Compute the MD5 hash of the floating-point number
    md5_hash = hashlib.md5(str(float_number).encode()).hexdigest()
    
    return md5_hash