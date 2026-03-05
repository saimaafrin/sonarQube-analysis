from collections import Counter
import random
LETTERS = ['a', 'b', 'c', 'd', 'e']
def task_func(count, seed=0):
    """
    Generate a specific number of random letter pairs, each from a predefined list, and analyze the frequency of each pair.
    """
    random.seed(seed)
    pairs = [random.choice(LETTERS) + random.choice(LETTERS) for _ in range(count)]
    counter = Counter(pairs)
    return counter