import base64
from cryptography.fernet import Fernet
def task_func(message, encryption_key):
    """
    Encrypts a message with a symmetric encryption key using Fernet encryption, and then encode the 
    encrypted message using base64.

    Parameters:
    message (str): The message to be encrypted and encoded.
    encryption_key (str): The key used for symmetric encryption. It should be a string, which will 
                          be encoded to bytes, then URL-safe base64 encoded to conform to the requirements 
                          for Fernet (32 bytes after encoding).

    Returns:
    str: The base64 encoded encrypted message. The message is first encrypted using Fernet encryption, 
         then the result is base64 encoded.

    Requirements:
    - base64
    - cryptography.fernet

    Example:
    >>> encrypted_message = task_func('Hello, World!', '01234567890123456789012345678901')
    >>> isinstance(encrypted_message, str)
    True
    """
    # Convert the encryption key to bytes
    encryption_key = bytes(encryption_key, 'utf-8')

    # Encrypt the message using Fernet
    f = Fernet(encryption_key)
    encrypted_message = f.encrypt(message.encode())

    # Encode the encrypted message using base64
    encrypted_message = base64.urlsafe_b64encode(encrypted_message)

    return encrypted_message