
import codecs
import random
import struct

KEYS = ['470FC614', '4A0FC614', '4B9FC614', '4C8FC614', '4D7FC614']

def task_func(hex_keys=KEYS):
    # Generate a random float number from the list of hex strings
    hex_key = random.choice(hex_keys)
    float_num = struct.unpack('f', bytes.fromhex(hex_key))[0]

    # Encode the float number in utf-8
    utf8_bytes = codecs.encode(str(float_num).encode('utf-8'), 'utf-8')

    return utf8_bytes