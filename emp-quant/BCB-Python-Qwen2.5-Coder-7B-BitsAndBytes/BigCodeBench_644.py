
import hashlib
import base64

def task_func(filename, data, password):
    # Create the directory if it doesn't exist
    import os
    directory = os.path.dirname(filename)
    if not os.path.exists(directory):
        os.makedirs(directory)

    # Encrypt the data using the password
    salt = os.urandom(16)
    key = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)
    iv = os.urandom(16)
    cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    ct_bytes = encryptor.update(data.encode('utf-8')) + encryptor.finalize()

    # Write the encrypted data and salt/iv to the file
    with open(filename, 'wb') as f:
        f.write(salt + iv + ct_bytes)

    # Return the encrypted string
    return base64.b64encode(ct_bytes).decode('utf-8')