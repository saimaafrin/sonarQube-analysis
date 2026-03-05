import string
import random
from collections import Counter
def task_func(n, seed=None):
    # Set the seed for random number generation if provided
    if seed is not None:
        random.seed(seed)
    
    # Generate a list of n random lowercase letters
    random_letters = [random.choice(string.ascii_lowercase) for _ in range(n)]
    
    # Count the occurrences of each letter in the list
    letter_counts = Counter(random_letters)
    
    # Return the Counter object containing the counts of each letter
    return letter_counts