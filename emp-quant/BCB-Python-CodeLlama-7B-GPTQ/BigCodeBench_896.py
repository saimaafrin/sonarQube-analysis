from collections import Counter
import random
import itertools
def task_func(length, count, seed=0):
    """
    Generate a number of random strings with a specified length from a fixed set of letters ('a', 'b', 'c', 'd', 'e'), and analyze the frequency of each letter in the generated strings.
    The function should output with:
        Counter: A collections.Counter object containing the frequency of each letter in the generated strings.
    """
    random.seed(seed)
    letters = 'abcde'
    strings = [random.sample(letters, length) for _ in range(count)]
    counter = Counter(itertools.chain.from_iterable(strings))
    return counter