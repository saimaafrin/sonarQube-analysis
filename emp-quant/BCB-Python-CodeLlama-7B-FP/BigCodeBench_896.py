from collections import Counter
import random
import itertools
def task_func(length, count, seed=0):
    """
    Generate a number of random strings with a specified length from a fixed set of letters ('a', 'b', 'c', 'd', 'e'), and analyze the frequency of each letter in the generated strings.
    """
    random.seed(seed)
    letters = ['a', 'b', 'c', 'd', 'e']
    strings = [random.choice(letters) for _ in range(length)]
    counter = Counter(itertools.chain.from_iterable(strings))
    return counter