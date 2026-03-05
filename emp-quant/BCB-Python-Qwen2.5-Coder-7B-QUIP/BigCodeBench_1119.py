
import codecs
import random
import string
import hashlib

def task_func(password_length=10, salt="salty"):
    # Generate a random password of the specified length
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(password_length))

    # Mix the password with the salt
    salted_password = salt + password

    # Hash the mixed password using SHA256
    hashed_password = hashlib.sha256(salted_password.encode()).hexdigest()

    # Return the hashed password as a string
    return str(hashed_password)