
from collections import Counter
import random
import itertools

def task_func(length, count, seed=0):
    # Set the random seed for reproducibility
    random.seed(seed)
    
    # Define the fixed set of letters
    letters = 'abcde'
    
    # Generate a list of random strings
    strings = [''.join(random.choices(letters, k=length)) for _ in range(count)]
    
    # Flatten the list of strings into a single list of characters
    all_chars = list(itertools.chain.from_iterable(strings))
    
    # Count the frequency of each letter
    letter_counter = Counter(all_chars)
    
    # Output the Counter object
    return letter_counter