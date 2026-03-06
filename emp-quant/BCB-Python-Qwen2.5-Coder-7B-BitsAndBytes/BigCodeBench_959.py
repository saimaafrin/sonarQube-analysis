
import string
import random

def task_func(text, seed=None):
    if seed is not None:
        random.seed(seed)
    
    alphabet_lower = string.ascii_lowercase
    alphabet_upper = string.ascii_uppercase
    
    result = []
    for char in text:
        if char.islower():
            result.append(random.choice(alphabet_lower))
        elif char.isupper():
            result.append(random.choice(alphabet_upper))
        else:
            result.append(char)
    
    return ''.join(result)