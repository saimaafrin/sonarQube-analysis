
import string
import random

def task_func(text, seed=None):
    random.seed(seed)
    output = ""
    for char in text:
        if char in string.ascii_letters:
            output += random.choice(string.ascii_letters)
        else:
            output += char
    return output