import random
import string
import base64
import zlib
def task_func(string_length=100):
    # Generate a random string of specified length
    random_string = ''.join(random.choices(string.ascii_uppercase + string.digits, k=string_length))
    
    # Compress the random string using zlib
    compressed_data = zlib.compress(random_string.encode('utf-8'))
    
    # Encode the compressed data in base64
    base64_encoded = base64.b64encode(compressed_data).decode('utf-8')
    
    return base64_encoded