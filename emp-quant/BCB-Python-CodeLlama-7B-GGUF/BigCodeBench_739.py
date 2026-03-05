
import struct
import random

# Constants
KEYS = ['470FC614', '4A0FC614', '4B9FC614', '4C8FC614', '4D7FC614']

def task_func(hex_key=None):
    # Generate a random hexadecimal string from the list of keys
    hex_key = random.choice(KEYS)

    # Convert the hexadecimal string to a float number
    float_num = struct.unpack('f', bytes.fromhex(hex_key))[0]

    # Round the float number to 2 decimal places
    rounded_float = round(float_num, 2)

    return rounded_float