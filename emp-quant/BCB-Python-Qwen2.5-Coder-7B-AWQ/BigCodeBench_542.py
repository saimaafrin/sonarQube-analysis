import hashlib
import random
import struct
KEYS = ['470FC614', '4A0FC614', '4B9FC614', '4C8FC614', '4D7FC614']
def task_func(hex_keys=KEYS, seed=42):
    # Set the seed for random number generation for deterministic results
    random.seed(seed)
    
    # Initialize a variable to store the selected hexadecimal string
    selected_hex = None
    
    # Loop until a valid hexadecimal string is selected
    while selected_hex is None:
        # Select a random hexadecimal string from the list
        selected_hex = random.choice(hex_keys)
        
        # Check if the selected string is a valid hexadecimal
        try:
            int(selected_hex, 16)
        except ValueError:
            # If not valid, reset the selected_hex to None and continue the loop
            selected_hex = None
    
    # Convert the selected hexadecimal string to a floating-point number
    float_number = struct.unpack('!f', bytes.fromhex(selected_hex))[0]
    
    # Compute the MD5 hash of the floating-point number
    md5_hash = hashlib.md5(str(float_number).encode()).hexdigest()
    
    # Return the MD5 hash as a string
    return md5_hash