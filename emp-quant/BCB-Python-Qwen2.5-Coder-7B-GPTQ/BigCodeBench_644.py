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
    cipher = Fernet(key)
    encrypted_data = cipher.encrypt(data.encode('utf-8'))

    # Write the encrypted data to the file
    with open(filename, 'wb') as file:
        file.write(salt + encrypted_data)

    # Return the encrypted string
    return encrypted_data.decode('utf-8')