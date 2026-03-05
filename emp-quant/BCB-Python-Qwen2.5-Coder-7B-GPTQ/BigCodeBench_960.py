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
            password.append(str(random.randint(0, 9)))
        elif char.isspace():
            choice = random.choice([string.ascii_lowercase, string.digits])
            password.append(random.choice(choice))
        else:
            password.append(char)
    
    return ''.join(password)