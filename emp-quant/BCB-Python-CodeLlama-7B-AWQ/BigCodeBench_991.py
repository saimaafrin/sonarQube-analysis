import binascii
import string
import random
def task_func(length):
    """
    Generate a random hexadecimal string of a given length and then attempt to decode it in ASCII.
    The resulting ASCII string may contain non-printable characters or be shorter than the input length.
    """
    # Generate a random hexadecimal string of the given length
    hex_string = ''.join(random.choice(string.hexdigits) for _ in range(length))

    # Attempt to decode the hexadecimal string in ASCII
    try:
        ascii_string = binascii.a2b_hex(hex_string)
    except binascii.Error:
        ascii_string = None

    # Return the decoded ASCII string
    return ascii_string