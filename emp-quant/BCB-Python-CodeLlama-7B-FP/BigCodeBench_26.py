import base64
from cryptography.fernet import Fernet
def task_func(message, encryption_key):
    """
    Encrypts a message with a symmetric encryption key using Fernet encryption,
    and then encode the encrypted message using base64.
    """
    # Encrypt the message using Fernet encryption
    fernet = Fernet(encryption_key)
    encrypted_message = fernet.encrypt(message.encode())

    # Encode the encrypted message using base64
    base64_encoded_message = base64.b64encode(encrypted_message)

    return base64_encoded_message
message = "Hello, World!"
encryption_key = "my_secret_key"