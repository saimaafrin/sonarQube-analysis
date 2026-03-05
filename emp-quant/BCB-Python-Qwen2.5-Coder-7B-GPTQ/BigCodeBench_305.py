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
    for sublist in list_of_lists:
        # If the sublist is empty, fill it with a random sample from the alphabet
        if not sublist:
            sublist = random.sample(ALPHABET, 1)
        
        # Count the frequency of each letter in the sublist
        letter_counter.update(sublist)
    
    # Return the Counter object with the frequency of each letter
    return letter_counter