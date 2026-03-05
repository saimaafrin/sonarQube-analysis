
import hashlib
import base64
import os

def task_func(filename, data, password):
    # Create directory if it does not exist
    directory = os.path.dirname(filename)
    if not os.path.exists(directory):
        os.makedirs(directory)

    # Encrypt the data using the password
    key = hashlib.sha256(password.encode()).digest()
    encrypted_data = base64.urlsafe_b64encode(key + data.encode()).decode()

    # Write the encrypted data to the file
    with open(filename, 'w') as file:
        file.write(encrypted_data)

    return encrypted_data