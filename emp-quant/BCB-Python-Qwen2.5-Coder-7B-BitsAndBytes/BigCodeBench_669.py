
import itertools
import math

def task_func(x):
    # Calculate the cosine of each value and sum them up for each key pair
    max_sum = float('-inf')
    best_pair = None
    
    for pair in itertools.combinations(x.keys(), 2):
        sum_cosine = math.cos(x[pair[0]]) + math.cos(x[pair[1]])
        if sum_cosine > max_sum:
            max_sum = sum_cosine
            best_pair = pair
            
    return best_pair