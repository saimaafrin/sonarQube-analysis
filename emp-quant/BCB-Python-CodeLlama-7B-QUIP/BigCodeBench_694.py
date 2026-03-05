
import itertools
import random

def task_func(t, n):
    combinations = itertools.combinations(t, n)
    random_combination = random.choice(list(combinations))
    return random_combination