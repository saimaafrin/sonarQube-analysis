
import hashlib
import base64
import os

def task_func(filename, data, password):
    # Encrypt the data with the password
    encrypted_data = hashlib.pbkdf2_hmac(
        'sha256',
        data.encode(),
        password.encode(),
        100000
    )

    # Encode the encrypted data in base64
    base64_data = base64.b64encode(encrypted_data)

    # Write the base64-encoded data to a file
    with open(filename, 'wb') as f:
        f.write(base64_data)

    # Return the encrypted string
    return base64_data.decode()

# Create the file if it does not exist
if not os.path.exists(filename):
    with open(filename, 'w'):
        pass

# Encrypt the data and write it to the file
encrypted_data = task_func(filename, data, password)

# Print the encrypted data
print(encrypted_data)