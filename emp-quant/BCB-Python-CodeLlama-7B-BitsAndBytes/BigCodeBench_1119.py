
import codecs
import random
import string
import hashlib

def task_func(password_length=10, salt="salty"):
    # Generate a random password
    password = ''.join(random.choice(string.ascii_letters + string.digits + string.punctuation) for _ in range(password_length))

    # Hash the password with SHA256
    hashed_password = hashlib.sha256(salt.encode() + password.encode()).hexdigest()

    return hashed_password