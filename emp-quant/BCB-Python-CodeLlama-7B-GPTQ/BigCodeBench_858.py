import string
import random
from collections import Counter
def task_func(n, seed=None):
    """
    Generate a number of random lowercase letters and count their occurrences.
    This function takes an integer input to determine how many random letters to generate and an optional seed for consistent randomness.
    It then creates a list of these letters, chosen from the English lowercase alphabet, and counts each letter's occurrences.
    The result is returned as a Counter object (from the collections module) which behaves like a dictionary where the keys are the letters, and the values are their counts.
    """
    if seed:
        random.seed(seed)
    letters = [random.choice(string.ascii_lowercase) for _ in range(n)]
    return Counter(letters)