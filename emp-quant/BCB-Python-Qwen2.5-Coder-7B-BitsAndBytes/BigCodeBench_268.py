
import collections
import random

# Constants
LETTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

def task_func(n_keys, n_values):
    # Create a dictionary with random keys from LETTERS and values as lists of consecutive integers
    result_dict = {}
    for _ in range(n_keys):
        key = random.choice(LETTERS)
        if key not in result_dict:
            result_dict[key] = list(range(1, n_values + 1))
    
    return result_dict