import string
import random
def task_func(text, seed=None):
    if not text:
        raise ValueError("Input text cannot be empty")
    
    if seed is not None:
        random.seed(seed)
    
    password = []
    for char in text:
        if char.isalpha():
            password.append(random.choice(string.ascii_lowercase))
        elif char.isdigit():
            password.append(random.choice(string.digits))
        elif char.isspace():
            choice = random.choice([string.digits, string.ascii_lowercase])
            password.append(random.choice(choice))
        else:
            password.append(char)
    
    return ''.join(password)