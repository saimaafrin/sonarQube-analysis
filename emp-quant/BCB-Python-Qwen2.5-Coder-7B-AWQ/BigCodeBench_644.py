import hashlib
import base64
import os
def task_func(filename, data, password):
    # Create directory if it does not exist
    directory = os.path.dirname(filename)
    if not os.path.exists(directory):
        os.makedirs(directory)

    # Encrypt the data
    encrypted_data = encrypt_data(data, password)

    # Write the encrypted data to the file
    with open(filename, 'wb') as file:
        file.write(encrypted_data)

    return encrypted_data
def encrypt_data(data, password):
    # Combine data and password
    combined = data + password

    # Create a hash of the combined data
    hash_object = hashlib.sha256(combined.encode())
    hash_bytes = hash_object.digest()

    # Encode the hash in base64
    encoded_hash = base64.b64encode(hash_bytes)

    return encoded_hash