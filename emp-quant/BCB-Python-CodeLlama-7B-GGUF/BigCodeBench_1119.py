
import codecs
import random
import string
import hashlib

def task_func(password_length=10, salt="salty"):
    # Generate a random password of the specified length
    password = ''.join(random.choice(string.ascii_letters + string.digits + string.punctuation) for _ in range(password_length))

    # Mix the password with the specified salt
    salted_password = password + salt

    # Hash the salted password using SHA256
    hashed_password = hashlib.sha256(salted_password.encode()).hexdigest()

    return hashed_password