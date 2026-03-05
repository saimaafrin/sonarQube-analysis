
import collections
import random

# Constants
LETTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

def task_func(n_keys, n_values):
    # Create a dictionary with random keys and values
    random_keys = random.sample(LETTERS, n_keys)
    random_values = [i for i in range(1, n_values + 1)]
    dict = collections.OrderedDict(zip(random_keys, random_values))
    return dict