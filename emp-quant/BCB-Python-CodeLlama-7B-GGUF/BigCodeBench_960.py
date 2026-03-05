
import string
import random

def task_func(text, seed=None):
    if not text:
        raise ValueError("Input text cannot be empty")

    password = ""
    for char in text:
        if char.isalpha():
            password += chr(random.randint(97, 122))
        elif char.isdigit():
            password += str(random.randint(0, 9))
        elif char.isspace():
            password += chr(random.randint(48, 57))
        else:
            password += char

    return password