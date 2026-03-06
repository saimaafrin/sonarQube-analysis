
import binascii
import string
import random

def task_func(length):
    # Generate a random hexadecimal string of the specified length
    hex_string = ''.join(random.choices(string.hexdigits[:-6], k=length))
    
    try:
        # Decode the hexadecimal string to ASCII
        ascii_string = bytes.fromhex(hex_string).decode('utf-8', errors='ignore')
    except binascii.Error:
        # Handle decoding error if the hex string is not valid
        ascii_string = ''
    
    return ascii_string