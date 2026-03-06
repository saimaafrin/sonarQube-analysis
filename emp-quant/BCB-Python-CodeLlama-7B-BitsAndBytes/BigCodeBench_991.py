
import binascii
import string
import random

def task_func(length):
    # Generate a random hexadecimal string of the given length
    hex_string = ''.join(random.choice(string.hexdigits) for _ in range(length))

    # Attempt to decode the hexadecimal string as ASCII
    try:
        ascii_string = binascii.a2b_hex(hex_string).decode('ascii')
    except binascii.Error:
        ascii_string = 'Invalid ASCII string'

    return ascii_string