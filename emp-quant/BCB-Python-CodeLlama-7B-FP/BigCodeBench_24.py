import base64
import hashlib
import os
def task_func(password, SALT_LENGTH = 32):
    """
    Hashes a password using the PBKDF2 HMAC algorithm with SHA-256 as the hashing algorithm, combined with a randomly generated salt, and returns both the salt and the hashed password, each base64-encoded.
    The function should raise the exception for: ValueError if the password is None or empty
    The function should output with:
        tuple[bytes, bytes]: A tuple containing the base64-encoded salt and the base64-encoded hashed password as byte strings.
    """
    if password is None or password == '':
        raise ValueError('Password cannot be None or empty')

    salt = os.urandom(SALT_LENGTH)
    hashed_password = hashlib.pbkdf2_hmac('sha256', password.encode(), salt, 100000)

    return base64.b64encode(salt), base64.b64encode(hashed_password)