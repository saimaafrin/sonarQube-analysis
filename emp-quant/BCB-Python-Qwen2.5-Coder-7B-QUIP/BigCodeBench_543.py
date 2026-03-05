
import base64
import os

def task_func():
    # Generate a random float number
    random_float = os.urandom(4)  # 4 bytes for a float
    # Convert the random float to a hexadecimal string
    hex_string = ''.join([format(x, '02x') for x in random_float])
    # Encode the hexadecimal string in base64
    base64_encoded = base64.b64encode(hex_string.encode('utf-8')).decode('utf-8')
    # Return the base64 encoded string
    return str(base64_encoded)