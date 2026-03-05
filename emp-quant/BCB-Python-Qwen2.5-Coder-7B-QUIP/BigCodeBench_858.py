
import string
import random
from collections import Counter

def task_func(n, seed=None):
    # Set the seed for random generation if provided
    if seed is not None:
        random.seed(seed)
    
    # Generate a list of n random lowercase letters
    letters = [random.choice(string.ascii_lowercase) for _ in range(n)]
    
    # Count the occurrences of each letter
    letter_counts = Counter(letters)
    
    # Return the Counter object
    return letter_counts