import itertools
import random
def task_func(t, n):
    # Generate all combinations of length n from the tuple t
    all_combinations = list(itertools.combinations(t, n))
    
    # Select a random combination from the list of all combinations
    random_combination = random.choice(all_combinations)
    
    # Return the random combination as a tuple
    return random_combination