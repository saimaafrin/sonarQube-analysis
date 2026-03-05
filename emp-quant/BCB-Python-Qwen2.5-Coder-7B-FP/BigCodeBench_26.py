import base64
from cryptography.fernet import Fernet
def task_func(message, encryption_key):
    # Ensure the encryption key is in bytes
    if isinstance(encryption_key, str):
        encryption_key = encryption_key.encode('utf-8')
    
    # Create a Fernet object with the provided encryption key
    fernet = Fernet(encryption_key)
    
    # Encrypt the message
    encrypted_message = fernet.encrypt(message.encode('utf-8'))
    
    # Encode the encrypted message in base64
    base64_encoded_message = base64.b64encode(encrypted_message)
    
    # Return the base64 encoded message as a string
    return base64_encoded_message.decode('utf-8')
encryption_key = Fernet.generate_key()
message = "Hello, World!"