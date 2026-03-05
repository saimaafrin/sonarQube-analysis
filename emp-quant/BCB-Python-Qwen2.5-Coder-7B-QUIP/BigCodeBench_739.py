
import struct
import random
# Constants
KEYS = ['470FC614', '4A0FC614', '4B9FC614', '4C8FC614', '4D7FC614']

def task_func(hex_key=None):
    # Convert the hexadecimal string to a float
    float_value = struct.unpack('!f', bytes.fromhex(hex_key))[0]
    
    # Round the float to 2 decimal places
    rounded_float = round(float_value, 2)
    
    return rounded_float