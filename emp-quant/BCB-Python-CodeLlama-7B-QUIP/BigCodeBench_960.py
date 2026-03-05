
import string
import random

def task_func(text, seed=None):
    if not text:
        raise ValueError("Input text is empty")

    random.seed(seed)

    result = ""
    for c in text:
        if c in string.ascii_lowercase:
            result += random.choice(string.ascii_lowercase)
        elif c in string.digits:
            result += str(random.randint(0, 9))
        elif c in string.whitespace:
            result += random.choice(string.ascii_lowercase + string.digits)
        else:
            result += c

    return result