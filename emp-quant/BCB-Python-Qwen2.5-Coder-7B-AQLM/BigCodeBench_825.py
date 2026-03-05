
import numpy as np
from itertools import product
import string

def task_func(length, seed=None, alphabets=list(string.ascii_lowercase)):
    if seed is not None:
        np.random.seed(seed)
    
    all_combinations = [''.join(p) for p in product(alphabets, repeat=length)]
    selected_combinations = np.random.choice(all_combinations, size=10, replace=False)
    
    return selected_combinations.tolist()