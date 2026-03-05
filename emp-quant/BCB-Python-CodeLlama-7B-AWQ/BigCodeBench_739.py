import struct
import random
KEYS = ['470FC614', '4A0FC614', '4B9FC614', '4C8FC614', '4D7FC614']
def task_func(hex_key=None):
    """
    Generate a random float number from a list of hexadecimal strings and then round the float number to 2 decimal places.
    """
    if hex_key is None:
        hex_key = random.choice(KEYS)
    # Convert hexadecimal string to float
    float_val = struct.unpack('f', bytes.fromhex(hex_key))[0]
    # Round float to 2 decimal places
    rounded_float = round(float_val, 2)
    return rounded_float