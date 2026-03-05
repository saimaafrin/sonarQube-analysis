import numpy as np
from itertools import product
import string
def task_func(length, seed=None, alphabets=list(string.ascii_lowercase)):
    """
    Generate a list of 10 randomly picked strings from all possible strings of a given length from the provided series of characters, using a specific seed for reproducibility.
    """
    if seed is not None:
        np.random.seed(seed)
    return np.random.choice(list(product(alphabets, repeat=length)), size=10, replace=False)