
import itertools
import random

def task_func(t, n):
    """
    Generate all combinations from a tuple with length n and return a random combination of length n.
    """
    combinations = list(itertools.combinations(t, n))
    random_combination = random.choice(combinations)
    return random_combination