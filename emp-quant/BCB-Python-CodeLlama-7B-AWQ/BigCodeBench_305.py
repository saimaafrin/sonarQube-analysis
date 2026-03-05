from collections import Counter
import itertools
import random
ALPHABET = 'abcdefghijklmnopqrstuvwxyz'
def task_func(list_of_lists, seed=0):
    """
    Count the frequency of each letter in a list of lists. If a list is empty, fill it with a random sample from the alphabet, and then count the letters.
    """
    # Create a Counter object to store the frequency of each letter
    counter = Counter()
    # Iterate over the list of lists
    for lst in list_of_lists:
        # If the list is empty, fill it with a random sample from the alphabet
        if not lst:
            lst = random.sample(ALPHABET, len(ALPHABET))
        # Iterate over the letters in the list
        for letter in lst:
            # Increment the frequency of the letter in the Counter object
            counter[letter] += 1
    # Return the Counter object
    return counter
list_of_lists = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f'],
    ['g', 'h', 'i'],
    ['j', 'k', 'l'],
    ['m', 'n', 'o'],
    ['p', 'q', 'r', 's'],
    ['t', 'u', 'v'],
    ['w', 'x', 'y', 'z']
]
seed = 0