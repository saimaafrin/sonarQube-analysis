import collections
import random
LETTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
def task_func(n_keys, n_values):
    # Create a dictionary with n_keys
    result_dict = {}
    
    # Select n_keys randomly from the LETTERS list
    selected_keys = random.sample(LETTERS, n_keys)
    
    # Assign consecutive integers starting from 1 as values
    for i in range(1, n_values + 1):
        # Randomly select a key from the selected_keys list
        key = random.choice(selected_keys)
        # Append the value to the list of values for the key in the dictionary
        if key in result_dict:
            result_dict[key].append(i)
        else:
            result_dict[key] = [i]
    
    return result_dict