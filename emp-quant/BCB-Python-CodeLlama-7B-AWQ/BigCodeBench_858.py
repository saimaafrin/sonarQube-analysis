import string
import random
from collections import Counter
def task_func(n, seed=None):
    """
    Generate a number of random lowercase letters and count their occurrences.

    Args:
        n (int): The number of random letters to generate.
        seed (int, optional): A seed for consistent randomness.

    Returns:
        Counter: A collections.Counter object with the count of each letter.
    """
    if seed is not None:
        random.seed(seed)

    # Generate a list of random lowercase letters
    letters = [random.choice(string.ascii_lowercase) for _ in range(n)]

    # Count the occurrences of each letter
    counter = Counter(letters)

    return counter