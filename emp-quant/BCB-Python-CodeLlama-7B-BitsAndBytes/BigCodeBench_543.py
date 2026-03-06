
import base64
import os

def task_func():
    # Generate a random float number
    random_float = random.random()

    # Convert the float to a hexadecimal string
    hex_string = hex(random_float)

    # Encode the hexadecimal string in base64
    base64_string = base64.b64encode(hex_string.encode('utf-8'))

    # Output the base64 encoded string
    print(base64_string.decode('utf-8'))

# Call the function
task_func()