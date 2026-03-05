
from collections import Counter
import itertools
import random
# Constants
ALPHABET = 'abcdefghijklmnopqrstuvwxyz'
def task_func(list_of_lists, seed=0):
    # Fill empty lists with random samples from the alphabet
    for lst in list_of_lists:
        if not lst:
            lst.extend(random.sample(ALPHABET, len(ALPHABET)))
    # Count the frequency of each letter
    counter = Counter()
    for lst in list_of_lists:
        for letter in lst:
            counter[letter] += 1
    return counter