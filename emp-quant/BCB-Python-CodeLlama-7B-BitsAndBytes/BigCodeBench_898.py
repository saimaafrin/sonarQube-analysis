
from collections import Counter
import random

LETTERS = ['a', 'b', 'c', 'd', 'e']

def task_func(count, seed=0):
    random.seed(seed)
    letter_pairs = []
    for _ in range(count):
        letter_pairs.append((random.choice(LETTERS), random.choice(LETTERS)))
    return Counter(letter_pairs)