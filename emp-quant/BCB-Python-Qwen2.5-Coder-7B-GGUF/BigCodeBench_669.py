
import itertools
import math

def task_func(x):
    # Calculate the cosine of each value in the dictionary
    cos_values = {key: math.cos(value) for key, value in x.items()}
    
    # Find the pair of keys with the highest sum of the cosine of their values
    max_sum = float('-inf')
    max_pair = None
    for pair in itertools.combinations(cos_values.keys(), 2):
        current_sum = cos_values[pair[0]] + cos_values[pair[1]]
        if current_sum > max_sum:
            max_sum = current_sum
            max_pair = pair
    
    return max_pair