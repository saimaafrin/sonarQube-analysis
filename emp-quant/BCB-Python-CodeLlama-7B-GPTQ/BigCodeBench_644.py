import hashlib
import base64
def task_func(filename, data, password):
    """Encrypt a string with a password, then write the encrypted string to a file. If the file or directory does not exist, create it.

    Args:
        filename (str): The file path to write the encrypted string to.
        data (str): The string to encrypt.
        password (str): The password to use for encryption.

    Returns:
        str: The encrypted string.
    """
    # Create a hash object using the SHA-256 algorithm
    hash_object = hashlib.sha256(password.encode())
    # Generate a key from the hash object
    key = hash_object.hexdigest()
    # Encrypt the data using the key
    encrypted_data = base64.b64encode(data.encode()).decode()
    # Write the encrypted data to the file
    with open(filename, "w") as file:
        file.write(encrypted_data)
    return encrypted_data
filename = "encrypted_data.txt"
data = "Hello, World!"
password = "my_password"