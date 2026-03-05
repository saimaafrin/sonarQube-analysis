import base64
import os
def task_func():
    # Generate a random float number between 0 and 1
    random_float = os.urandom(4)  # Generate 4 random bytes
    random_float = struct.unpack('!f', random_float)[0]  # Convert bytes to float

    # Convert the float to a hexadecimal string
    hex_string = format(struct.unpack('!I', struct.pack('!f', random_float))[0], '08x')

    # Encode the hexadecimal string in base64
    base64_encoded = base64.b64encode(hex_string.encode('utf-8')).decode('utf-8')

    return base64_encoded