import hashlib
import base64
def task_func(filename, data, password):
    """
    Encrypt a string with a password, then write the encrypted string to a file.
    If the file or directory does not exist, create it.
    """
    # Create a hash object using the SHA-256 algorithm
    hash_object = hashlib.sha256(password.encode())
    # Get the hash value as a byte string
    hash_value = hash_object.digest()
    # Create a base64 encoder
    encoder = base64.encoder()
    # Encode the hash value
    encoded_hash = encoder.encode(hash_value)
    # Create a cipher object using the AES-256 algorithm
    cipher = AES.new(encoded_hash, AES.MODE_CBC)
    # Encrypt the data
    encrypted_data = cipher.encrypt(data.encode())
    # Write the encrypted data to a file
    with open(filename, "wb") as file:
        file.write(encrypted_data)
    # Return the encrypted string
    return encrypted_data.decode()
filename = "test.txt"
data = "Hello, World!"
password = "my_secret_password"