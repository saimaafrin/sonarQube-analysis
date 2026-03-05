
import binascii
import string
import random

def task_func(length):
    # Generate a random hexadecimal string of the given length
    hex_string = ''.join(random.choice(string.hexdigits) for _ in range(length))

    # Attempt to decode the hexadecimal string as ASCII
    try:
        ascii_string = binascii.unhexlify(hex_string).decode('ascii')
    except binascii.Error:
        # If the decoding fails, return an empty string
        ascii_string = ''

    return ascii_string