
import collections
import random
# Constants
LETTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

def task_func(n_keys, n_values):
    # Generate a list of n_keys random letters
    keys = [random.choice(LETTERS) for _ in range(n_keys)]
    
    # Create a dictionary with keys and values
    result_dict = {key: [i for i in range(1, n_values + 1)] for key in keys}
    
    return result_dict