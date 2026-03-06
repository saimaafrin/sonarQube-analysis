
import base64
from cryptography.fernet import Fernet

def generate_key():
    """Generate a new Fernet key."""
    return Fernet.generate_key()

def task_func(message, encryption_key):
    """
    Encrypts a message with a symmetric encryption key using Fernet encryption,
    and then encodes the encrypted message using base64.

    :param message: str, the message to be encrypted
    :param encryption_key: bytes, the Fernet key used for encryption
    :return: str, the base64 encoded encrypted message
    """
    # Ensure the encryption key is of type bytes
    if not isinstance(encryption_key, bytes):
        raise ValueError("Encryption key must be of type bytes")
    
    # Create a Fernet object with the provided key
    fernet = Fernet(encryption_key)
    
    # Encode the message to bytes
    message_bytes = message.encode('utf-8')
    
    # Encrypt the message
    encrypted_message = fernet.encrypt(message_bytes)
    
    # Encode the encrypted message to base64
    base64_encoded_message = base64.b64encode(encrypted_message).decode('utf-8')
    
    return base64_encoded_message

    # Message to encrypt
    message = "Hello, World!"
    
    # Encrypt the message
    encrypted_base64_message = task_func(message, key)
    
    print(f"Encrypted Base64 Message: {encrypted_base64_message}")