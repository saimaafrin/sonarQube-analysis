
from collections import Counter
import itertools
import random
# Constants
ALPHABET = 'abcdefghijklmnopqrstuvwxyz'
def task_func(list_of_lists, seed=0):
    # Set the random seed for reproducibility
    random.seed(seed)
    
    # Initialize a Counter object
    letter_counter = Counter()
    
    # Iterate over each list in the list of lists
    for sublist in list_of_lists:
        # If the sublist is empty, replace it with a random sample from the alphabet
        if not sublist:
            sublist = list(itertools.islice(itertools.cycle(ALPHABET), 26))
        
        # Count the letters in the sublist
        for letter in sublist:
            letter_counter[letter] += 1
    
    # Return the Counter object
    return letter_counter