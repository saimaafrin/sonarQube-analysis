import base64
import os
def task_func():
    # Generate a random float number between 0 and 1
    random_float = os.urandom(4)
    # Convert the random float to a hexadecimal string
    hex_string = random_float.hex()
    # Encode the hexadecimal string in base64
    base64_encoded = base64.b64encode(hex_string.encode('utf-8')).decode('utf-8')
    return base64_encoded