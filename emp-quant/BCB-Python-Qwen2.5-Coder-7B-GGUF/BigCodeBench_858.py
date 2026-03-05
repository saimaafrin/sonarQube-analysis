
import string
import random
from collections import Counter

def task_func(n, seed=None):
    if seed is not None:
        random.seed(seed)
    
    # Generate a list of n random lowercase letters
    random_letters = [random.choice(string.ascii_lowercase) for _ in range(n)]
    
    # Count the occurrences of each letter
    letter_counts = Counter(random_letters)
    
    return letter_counts