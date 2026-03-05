
import hashlib
import base64

def task_func(filename, data, password):
    # Create the hash object
    hash_obj = hashlib.sha256()

    # Update the hash object with the data
    hash_obj.update(data)

    # Hash the data with the password
    hash_obj.update(password.encode())

    # Get the encrypted string
    encrypted_string = hash_obj.hexdigest()

    # Write the encrypted string to the file
    with open(filename, "w") as f:
        f.write(encrypted_string)

    return encrypted_string