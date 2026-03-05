
from collections import Counter
import random
import itertools

def task_func(length, count, seed=0):
    random.seed(seed)
    strings = [random.choice('abcd') for _ in range(count)]
    counter = Counter(c for s in strings for c in s)
    return counter