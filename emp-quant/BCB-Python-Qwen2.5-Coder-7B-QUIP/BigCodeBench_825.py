
import numpy as np
from itertools import product
import string
def task_func(length, seed=None, alphabets=list(string.ascii_lowercase)):
    # Set the seed for reproducibility
    np.random.seed(seed)
    
    # Generate all possible strings of the given length from the provided alphabets
    all_strings = list(product(alphabets, repeat=length))
    
    # Select 10 random strings from the list
    selected_strings = np.random.choice(all_strings, size=10, replace=False)
    
    # Convert the selected strings to a list of strings
    selected_strings = [''.join(x) for x in selected_strings]
    
    return selected_strings