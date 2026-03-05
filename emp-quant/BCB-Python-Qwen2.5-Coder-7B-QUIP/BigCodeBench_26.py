
import base64
from cryptography.fernet import Fernet

def task_func(message, encryption_key):
    # Create a Fernet key from the provided encryption key
    fernet = Fernet(encryption_key)
    
    # Encrypt the message using the Fernet key
    encrypted_message = fernet.encrypt(message.encode())
    
    # Encode the encrypted message in base64
    base64_encoded_message = base64.b64encode(encrypted_message)
    
    # Return the base64 encoded message as a string
    return base64_encoded_message.decode('utf-8')