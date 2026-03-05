import string
import random
from collections import Counter
def task_func(n, seed=None):
    """
    Generate a list of n random lowercase letters and count their occurrences.
    
    Parameters:
    n (int): The number of random letters to generate.
    seed (int, optional): A seed for the random number generator for consistent results.
    
    Returns:
    Counter: A collections.Counter object with the count of each letter.
    """
    if seed is not None:
        random.seed(seed)
    
    # Generate a list of n random lowercase letters
    random_letters = [random.choice(string.ascii_lowercase) for _ in range(n)]
    
    # Count the occurrences of each letter
    letter_counts = Counter(random_letters)
    
    return letter_counts