import collections
import random
LETTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
def task_func(n_keys, n_values):
    # Create a dictionary with random keys and consecutive integer values
    result_dict = {random.choice(LETTERS): list(range(1, n_values + 1)) for _ in range(n_keys)}
    return result_dict