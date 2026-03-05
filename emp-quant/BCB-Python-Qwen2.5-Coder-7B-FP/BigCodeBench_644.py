import hashlib
import base64
import os
def task_func(filename, data, password):
    # Create directory if it does not exist
    directory = os.path.dirname(filename)
    if not os.path.exists(directory):
        os.makedirs(directory)

    # Encrypt the data using the password
    salt = os.urandom(16)
    key = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)
    encrypted_data = base64.b64encode(key + salt + data.encode('utf-8')).decode('utf-8')

    # Write the encrypted data to the file
    with open(filename, 'w') as file:
        file.write(encrypted_data)

    return encrypted_data