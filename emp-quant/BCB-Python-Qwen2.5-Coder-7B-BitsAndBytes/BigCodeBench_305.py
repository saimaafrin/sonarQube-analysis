
from collections import Counter
import itertools
import random

# Constants
ALPHABET = 'abcdefghijklmnopqrstuvwxyz'

def task_func(list_of_lists, seed=0):
    # Set the random seed for reproducibility
    random.seed(seed)
    
    # Flatten the list of lists and handle empty lists
    flattened_list = []
    for sublist in list_of_lists:
        if not sublist:
            # Fill empty list with a random sample from the alphabet
            sublist = [random.choice(ALPHABET) for _ in range(10)]  # Assuming we want 10 characters
        flattened_list.extend(sublist)
    
    # Count the frequency of each letter
    letter_counter = Counter(flattened_list)
    
    return letter_counter