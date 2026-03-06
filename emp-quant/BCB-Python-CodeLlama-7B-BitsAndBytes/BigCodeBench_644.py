
import hashlib
import base64
import os

def task_func(filename, data, password):
    # Encrypt the data with the password
    encrypted_data = hashlib.pbkdf2_hmac(password.encode(), data.encode(), 100000)

    # Encode the encrypted data in base64
    encrypted_data_base64 = base64.b64encode(encrypted_data)

    # Write the encrypted data to a file
    with open(filename, 'wb') as f:
        f.write(encrypted_data_base64)

    return encrypted_data_base64.decode()