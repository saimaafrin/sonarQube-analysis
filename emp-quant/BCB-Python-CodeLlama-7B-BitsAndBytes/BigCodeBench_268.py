
import collections
import random

# Constants
LETTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

def task_func(n_keys, n_values):
    # Create a dictionary with n_keys random keys and n_values values for each key
    d = collections.defaultdict(list)
    for i in range(n_keys):
        key = random.choice(LETTERS)
        value = random.randint(1, n_values)
        d[key].append(value)
    return d