import base64
from cryptography.fernet import Fernet
def task_func(message, encryption_key):
    # Ensure the encryption key is in bytes
    if isinstance(encryption_key, str):
        encryption_key = encryption_key.encode()
    
    # Create a Fernet instance with the provided encryption key
    fernet = Fernet(encryption_key)
    
    # Encrypt the message
    encrypted_message = fernet.encrypt(message.encode())
    
    # Encode the encrypted message in base64
    base64_encoded_message = base64.b64encode(encrypted_message)
    
    # Return the base64 encoded encrypted message as a string
    return base64_encoded_message.decode()