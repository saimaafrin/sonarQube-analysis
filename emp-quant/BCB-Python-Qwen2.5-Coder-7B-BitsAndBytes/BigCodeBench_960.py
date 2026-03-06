
import string
import random

def task_func(text, seed=None):
    if not text:
        raise ValueError("Input text cannot be empty")
    
    if seed is not None:
        random.seed(seed)
    
    result = []
    for char in text:
        if char.isalpha():
            result.append(random.choice(string.ascii_lowercase))
        elif char.isdigit():
            result.append(str(random.randint(0, 9)))
        elif char == ' ':
            choice = random.choice([string.digits, string.ascii_lowercase])
            result.append(random.choice(choice))
        else:
            result.append(char)
    
    return ''.join(result)