
import numpy as np
from itertools import product
import string

def task_func(length, seed=None, alphabets=list(string.ascii_lowercase)):
    if seed is not None:
        np.random.seed(seed)
    
    # Generate all possible strings of the given length
    all_strings = [''.join(p) for p in product(alphabets, repeat=length)]
    
    # Randomly pick 10 strings without replacement
    selected_strings = np.random.choice(all_strings, size=10, replace=False).tolist()
    
    return selected_strings