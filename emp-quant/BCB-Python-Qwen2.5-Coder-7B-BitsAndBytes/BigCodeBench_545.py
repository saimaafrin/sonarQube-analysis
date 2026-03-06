
import codecs
import random
import struct

KEYS = ['470FC614', '4A0FC614', '4B9FC614', '4C8FC614', '4D7FC614']

def task_func(hex_keys=KEYS):
    # Convert hex strings to integers
    int_keys = [int(key, 16) for key in hex_keys]
    
    # Select a random integer from the list
    selected_int = random.choice(int_keys)
    
    # Convert the integer to a float
    float_number = struct.unpack('!f', struct.pack('!I', selected_int))[0]
    
    # Encode the float number as UTF-8
    utf8_encoded_float = codecs.encode(str(float_number), 'utf-8')
    
    return utf8_encoded_float