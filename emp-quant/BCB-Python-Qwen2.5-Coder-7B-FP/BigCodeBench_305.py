from collections import Counter
import itertools
import random
ALPHABET = 'abcdefghijklmnopqrstuvwxyz'
def task_func(list_of_lists, seed=0):
    # Set the seed for random number generation
    random.seed(seed)
    
    # Initialize a Counter object to store the frequency of each letter
    letter_counter = Counter()
    
    # Iterate over each list in the list of lists
    for lst in list_of_lists:
        # If the list is empty, fill it with a random sample from the alphabet
        if not lst:
            lst = random.sample(ALPHABET, 1)
        
        # Count the frequency of each letter in the list and update the Counter object
        letter_counter.update(lst)
    
    # Return the Counter object
    return letter_counter