
import itertools
import random

def task_func(t, n):
    # Generate all combinations of length n from the tuple
    combinations = list(itertools.combinations(t, n))
    
    # Select a random combination from the list of combinations
    random_combination = random.choice(combinations)
    
    return random_combination