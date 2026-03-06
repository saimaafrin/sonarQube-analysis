
import struct
import random

# Constants
KEYS = ['470FC614', '4A0FC614', '4B9FC614', '4C8FC614', '4D7FC614']

def task_func(hex_key=None):
    # Generate a random hexadecimal string from the list of keys
    hex_string = random.choice(KEYS)

    # Convert the hexadecimal string to a float
    float_value = struct.unpack('f', bytes.fromhex(hex_string))[0]

    # Round the float value to 2 decimal places
    rounded_float = round(float_value, 2)

    # Output the rounded float value
    print(rounded_float)

# Call the function with a random hexadecimal string as an argument
task_func(hex_key='4B9FC614')