
from collections import Counter
import itertools
import random

# Constants
ALPHABET = 'abcdefghijklmnopqrstuvwxyz'

def task_func(list_of_lists, seed=0):
    random.seed(seed)
    
    # Fill empty lists with random samples from the alphabet
    for sublist in list_of_lists:
        if not sublist:
            sublist.extend(random.sample(ALPHABET, 10))
    
    # Flatten the list of lists into a single list
    flattened_list = list(itertools.chain.from_iterable(list_of_lists))
    
    # Count the frequency of each letter
    letter_frequency = Counter(flattened_list)
    
    return letter_frequency