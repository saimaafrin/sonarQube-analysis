import random
import string
import base64
import zlib
def task_func(string_length=100):
    """
    Create a random string of a specified length with uppercase letters and digits, compress it with zlib, and then encode the compressed string in base64.
    """
    # Generate a random string with uppercase letters and digits
    random_string = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(string_length))

    # Compress the random string with zlib
    compressed_string = zlib.compress(random_string.encode())

    # Encode the compressed string in base64
    base64_string = base64.b64encode(compressed_string).decode()

    return base64_string