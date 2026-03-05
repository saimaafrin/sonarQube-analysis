import itertools
import random
def task_func(t, n):
    """
    Generate all combinations from a tuple with length n and return a random combination of length n.
    """
    combinations = itertools.combinations(t, n)
    return random.choice(list(combinations))
t = (1, 2, 3, 4, 5)
n = 3