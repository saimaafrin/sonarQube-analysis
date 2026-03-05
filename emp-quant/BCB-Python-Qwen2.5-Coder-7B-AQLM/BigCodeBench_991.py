
import binascii
import string
import random

def task_func(length):
    # Generate a random hexadecimal string of the given length
    hex_string = ''.join(random.choices(string.hexdigits.lower(), k=length))
    
    # Attempt to decode the hexadecimal string in ASCII
    try:
        ascii_string = binascii.unhexlify(hex_string).decode('ascii')
    except binascii.Error:
        ascii_string = ''
    
    return ascii_string