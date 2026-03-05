
import codecs
import random
import struct
KEYS = ['470FC614', '4A0FC614', '4B9FC614', '4C8FC614', '4D7FC614']
def task_func(hex_keys=KEYS):
    # Convert the first 8 characters of a random key to an integer
    random_key = random.choice(hex_keys)
    int_value = int(random_key[:8], 16)
    
    # Convert the integer to a float
    float_value = struct.unpack('f', struct.pack('I', int_value))[0]
    
    # Encode the float in utf-8
    utf_8_encoded = codecs.encode(str(float_value), 'utf-8')
    
    # Output the utf-8 encoded bytes
    print(f"bytes: {utf_8_encoded}")