
from collections import Counter
import itertools
import random

# Constants
ALPHABET = 'abcdefghijklmnopqrstuvwxyz'

def task_func(list_of_lists, seed=0):
    random.seed(seed)
    # Flatten the list of lists and handle empty lists
    flattened_list = []
    for sublist in list_of_lists:
        if not sublist:
            flattened_list.extend(random.sample(ALPHABET, 1))
        else:
            flattened_list.extend(sublist)
    
    # Count the frequency of each letter
    letter_frequency = Counter(flattened_list)
    
    return letter_frequency