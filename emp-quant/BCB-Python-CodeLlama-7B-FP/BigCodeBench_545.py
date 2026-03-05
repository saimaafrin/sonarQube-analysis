import codecs
import random
import struct
KEYS = ['470FC614', '4A0FC614', '4B9FC614', '4C8FC614', '4D7FC614']
def task_func(hex_keys=KEYS):
    """
    Generate a random float number from a list of hex strings and then encode the float number in utf-8.
    """
    # Generate a random hex string from the list of hex strings
    hex_string = random.choice(hex_keys)

    # Convert the hex string to a float number
    float_number = struct.unpack('f', bytes.fromhex(hex_string))[0]

    # Encode the float number in utf-8
    utf8_bytes = codecs.encode(float_number, 'utf-8')

    # Return the utf-8 encoded float number
    return utf8_bytes