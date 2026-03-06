
import base64
from cryptography.fernet import Fernet

def task_func(message, encryption_key):
    # Encrypt the message using Fernet encryption
    f = Fernet(encryption_key)
    encrypted_message = f.encrypt(message.encode())

    # Encode the encrypted message using base64
    base64_encoded_message = base64.b64encode(encrypted_message)

    # Return the base64 encoded encrypted message
    return base64_encoded_message

# Encrypt and base64 encode the message
encrypted_message = task_func(message, encryption_key)

# Print the encrypted message
print(encrypted_message)