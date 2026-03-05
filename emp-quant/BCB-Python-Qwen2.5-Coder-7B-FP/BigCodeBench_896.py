from collections import Counter
import random
import itertools
def task_func(length, count, seed=0):
    # Set the random seed for reproducibility
    random.seed(seed)
    
    # Define the fixed set of letters
    letters = 'abcde'
    
    # Generate the random strings
    random_strings = [''.join(random.choice(letters) for _ in range(length)) for _ in range(count)]
    
    # Flatten the list of strings into a single string
    all_letters = ''.join(random_strings)
    
    # Count the frequency of each letter
    letter_frequency = Counter(all_letters)
    
    return letter_frequency