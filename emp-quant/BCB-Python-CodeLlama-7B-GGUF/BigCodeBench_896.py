
from collections import Counter
import random
import itertools

def task_func(length, count, seed=0):
    random.seed(seed)
    strings = [random.choice('abcde') for _ in range(count)]
    counter = Counter(itertools.chain.from_iterable(strings))
    return counter