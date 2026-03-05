import random
from collections import Counter
from statistics import mode
def task_func(list_length=1000, range_start=1, range_end=10, random_seed=None):
    """
    Generate a random list of integers within a specified range.
    Convert this list to a generator object that yields tuples.
    Each tuple contains a number from the list and its frequency.
    Additionally, find and return the mode of the list.
    """
    if random_seed is not None:
        random.seed(random_seed)
    numbers = random.sample(range(range_start, range_end + 1), list_length)
    counter = Counter(numbers)
    mode = mode(numbers)