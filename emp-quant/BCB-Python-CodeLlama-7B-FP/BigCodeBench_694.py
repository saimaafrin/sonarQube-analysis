import itertools
import random
def task_func(t, n):
    """
    Generate all combinations from a tuple with length n and return a random combination of length n.
    """
    combinations = itertools.combinations(t, n)
    random_combination = random.choice(list(combinations))
    return random_combination
t = (1, 2, 3)
n = 2