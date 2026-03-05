
import base64
from cryptography.fernet import Fernet

def task_func(message, encryption_key):
    # Encrypt the message using Fernet
    fernet = Fernet(encryption_key)
    encrypted_message = fernet.encrypt(message.encode())

    # Base64 encode the encrypted message
    base64_encoded_message = base64.b64encode(encrypted_message)

    # Return the base64 encoded message
    return base64_encoded_message.decode()