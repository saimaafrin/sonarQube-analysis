
import numpy as np
from itertools import product
import string

def task_func(length, seed=None, alphabets=list(string.ascii_lowercase)):
    if seed:
        np.random.seed(seed)
    return np.random.choice(list(product(alphabets, repeat=length)), size=10)