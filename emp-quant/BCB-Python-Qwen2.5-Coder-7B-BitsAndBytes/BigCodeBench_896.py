
from collections import Counter
import random

def task_func(length, count, seed=0):
    # Set the random seed for reproducibility
    random.seed(seed)
    
    # Define the fixed set of letters
    letters = ['a', 'b', 'c', 'd', 'e']
    
    # Generate the random strings
    random_strings = [''.join(random.choices(letters, k=length)) for _ in range(count)]
    
    # Concatenate all strings into one string
    combined_string = ''.join(random_strings)
    
    # Count the frequency of each letter
    letter_frequency = Counter(combined_string)
    
    return letter_frequency