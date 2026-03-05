
import string
import random

BRACKETS = "(){}[]"

def task_func(length, random_seed=None):
    if random_seed is not None:
        random.seed(random_seed)
    
    characters = BRACKETS + string.ascii_lowercase
    result = ''.join(random.choice(characters) for _ in range(length))
    
    return result

string = task_func(23, random_seed=1)
print(string)  # Output: ieqh]{[yng]by)a{rogubbb