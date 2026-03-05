
import base64
from cryptography.fernet import Fernet

def task_func(message, encryption_key):
    # Encrypt the message with Fernet
    f = Fernet(encryption_key)
    encrypted_message = f.encrypt(message)

    # Encode the encrypted message with base64
    base64_encoded_message = base64.b64encode(encrypted_message)

    return base64_encoded_message