
import random
import string
import base64
import zlib

def task_func(string_length=100):
    # Generate a random string of the specified length
    random_string = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(string_length))

    # Compress the string with zlib
    compressed_string = zlib.compress(random_string)

    # Encode the compressed string in base64
    base64_string = base64.b64encode(compressed_string)

    return base64_string