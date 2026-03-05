import string
import random
BRACKETS = "(){}[]"
def task_func(length, random_seed=None):
    if random_seed is not None:
        random.seed(random_seed)
    
    # Combine the set of brackets and lowercase English characters
    characters = BRACKETS + string.ascii_lowercase
    
    # Generate a random string of the specified length
    result = ''.join(random.choice(characters) for _ in range(length))
    
    return result