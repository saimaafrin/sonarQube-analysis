import hashlib
import base64
def task_func(filename, data, password):
    """
    Encrypts a string with a password and writes the encrypted string to a file.
    If the file or directory does not exist, create it.
    """
    # Create a hash object
    hash_object = hashlib.sha256(password.encode())
    # Get the hash value
    hash_value = hash_object.hexdigest()
    # Create a base64 object
    base64_object = base64.b64encode(data.encode())
    # Get the base64 value
    base64_value = base64_object.decode()
    # Create a file object
    file_object = open(filename, "wb")
    # Write the encrypted string to the file
    file_object.write(base64_value.encode())
    # Close the file object
    file_object.close()
    # Return the encrypted string
    return base64_value
filename = "test.txt"
data = "Hello, World!"
password = "secret"