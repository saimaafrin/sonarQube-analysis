from collections import Counter
import random
LETTERS = ['a', 'b', 'c', 'd', 'e']
def task_func(count, seed=0):
    """
    Generate a specific number of random letter pairs, each from a predefined list, and analyze the frequency of each pair.
    The function should output with:
        Counter: A Counter object representing the frequency of each generated letter pair.
    """
    random.seed(seed)
    pairs = []
    for _ in range(count):
        pair = (random.choice(LETTERS), random.choice(LETTERS))
        pairs.append(pair)
    counter = Counter(pairs)
    return counter