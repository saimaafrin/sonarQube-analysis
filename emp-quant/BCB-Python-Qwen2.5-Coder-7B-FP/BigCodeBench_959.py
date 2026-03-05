import string
import random
def task_func(text, seed=None):
    if seed is not None:
        random.seed(seed)
    
    alphabet_lower = string.ascii_lowercase
    alphabet_upper = string.ascii_uppercase
    
    transformed_text = []
    
    for char in text:
        if char.islower():
            transformed_text.append(random.choice(alphabet_lower))
        elif char.isupper():
            transformed_text.append(random.choice(alphabet_upper))
        else:
            transformed_text.append(char)
    
    return ''.join(transformed_text)