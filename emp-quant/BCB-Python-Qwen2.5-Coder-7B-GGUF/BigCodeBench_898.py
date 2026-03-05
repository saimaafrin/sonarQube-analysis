
from collections import Counter
import random
LETTERS = ['a', 'b', 'c', 'd', 'e']

def task_func(count, seed=0):
    random.seed(seed)
    letter_pairs = [random.choice(LETTERS) + random.choice(LETTERS) for _ in range(count)]
    return Counter(letter_pairs)