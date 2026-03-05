
import itertools
import random

def task_func(t, n):
    # Generate all combinations of the input tuple t of length n
    all_combinations = list(itertools.combinations(t, n))
    
    # Select a random combination from the list of all combinations
    random_combination = random.choice(all_combinations)
    
    # Output the random combination
    print(f"tuple: {random_combination}")