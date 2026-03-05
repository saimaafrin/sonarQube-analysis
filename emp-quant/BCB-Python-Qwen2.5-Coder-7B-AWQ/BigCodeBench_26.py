import base64
from cryptography.fernet import Fernet
def task_func(message, encryption_key):
    # Create a Fernet object with the provided encryption key
    fernet = Fernet(encryption_key)
    
    # Encrypt the message using the Fernet object
    encrypted_message = fernet.encrypt(message.encode())
    
    # Encode the encrypted message using base64
    base64_encoded_message = base64.b64encode(encrypted_message)
    
    # Return the base64 encoded message as a string
    return base64_encoded_message.decode()
message = "Hello, world!"
encryption_key = Fernet.generate_key()