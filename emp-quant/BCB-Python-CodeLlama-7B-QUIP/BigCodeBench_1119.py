
import codecs
import random
import string
import hashlib

def task_func(password_length=10, salt="salty"):
    password = "".join(random.choice(string.ascii_letters + string.digits + string.punctuation) for _ in range(password_length))
    hashed_password = hashlib.sha256(salt + password).hexdigest()
    return hashed_password