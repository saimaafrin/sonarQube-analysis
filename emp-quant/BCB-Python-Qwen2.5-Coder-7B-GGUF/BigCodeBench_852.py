
import random
import string

def task_func(max_length, n_samples, seed=None):
    if max_length < 1:
        raise ValueError("max_length must be at least 1")
    
    if seed is not None:
        random.seed(seed)
    
    result = []
    for _ in range(n_samples):
        length = random.randint(1, max_length)
        random_string = ''.join(random.choices(string.ascii_lowercase, k=length))
        result.append(random_string)
    
    return result