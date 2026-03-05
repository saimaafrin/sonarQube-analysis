import numpy as np
from itertools import product
import string
def task_func(length, seed=None, alphabets=list(string.ascii_lowercase)):
    """
    Generate a list of 10 randomly picked strings from all possible strings of a given length from the provided series of characters, using a specific seed for reproducibility.
    """
    np.random.seed(seed)
    all_strings = list(product(alphabets, repeat=length))
    return np.random.choice(all_strings, size=10, replace=False).tolist()