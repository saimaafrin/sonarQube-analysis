
import random
import string
import base64
import zlib

def task_func(string_length=100):
    # Generate a random string of the specified length
    random_string = ''.join(random.choices(string.ascii_uppercase + string.digits, k=string_length))
    
    # Compress the string using zlib
    compressed_string = zlib.compress(random_string.encode('utf-8'))
    
    # Encode the compressed string in base64
    base64_string = base64.b64encode(compressed_string)
    
    # Return the base64 encoded string
    return base64_string.decode('utf-8')