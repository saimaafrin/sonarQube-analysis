
import string
import random
from collections import Counter

def task_func(n, seed=None):
    """
    Generate a number of random lowercase letters and count their occurrences.

    Args:
        n (int): Number of random letters to generate.
        seed (int, optional): Seed for consistent randomness. Defaults to None.

    Returns:
        Counter: A collections.Counter object with the count of each letter.
    """
    if seed is not None:
        random.seed(seed)

    letters = [random.choice(string.ascii_lowercase) for _ in range(n)]
    return Counter(letters)