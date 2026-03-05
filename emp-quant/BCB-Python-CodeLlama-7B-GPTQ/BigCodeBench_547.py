import hashlib
import os
import base64
def task_func(password: str, salt_length: int = 8) -> str:
    """
    Encrypt a password using Salt and SHA-256, then encode the result in base64.
    :param password: The password to encrypt.
    :param salt_length: The length of the salt.
    :return: The encrypted password in base64 format.
    """
    salt = os.urandom(salt_length)
    hash = hashlib.sha256(salt + password.encode()).hexdigest()
    return base64.b64encode(salt + hash.encode()).decode()