import struct
import random
def task_func(hex_key=None):
    # Convert the hexadecimal string to a float
    float_value = struct.unpack('!f', bytes.fromhex(hex_key))[0]
    
    # Round the float number to 2 decimal places
    rounded_float = round(float_value, 2)
    
    return rounded_float