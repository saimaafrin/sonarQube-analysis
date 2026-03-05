
from collections import Counter
import random
LETTERS = ['a', 'b', 'c', 'd', 'e']
def task_func(count, seed=0):
    random.seed(seed)
    pairs = [random.sample(LETTERS, 2) for _ in range(count)]
    counter = Counter(pairs)
    return counter