
from collections import Counter
import itertools
import random
# Constants
ALPHABET = 'abcdefghijklmnopqrstuvwxyz'
def task_func(list_of_lists, seed=0):
    # Initialize the counter
    counter = Counter()
    # Loop through the list of lists
    for lst in list_of_lists:
        # Check if the list is empty
        if lst:
            # If not empty, count the letters
            for c in lst:
                counter[c] += 1
        else:
            # If empty, fill it with a random sample from the alphabet
            lst = random.sample(ALPHABET, len(lst))
            # Count the letters in the random sample
            for c in lst:
                counter[c] += 1
    return counter