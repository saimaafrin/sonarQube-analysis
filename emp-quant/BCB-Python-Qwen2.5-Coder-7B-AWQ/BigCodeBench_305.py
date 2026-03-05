from collections import Counter
import itertools
import random
ALPHABET = 'abcdefghijklmnopqrstuvwxyz'
def task_func(list_of_lists, seed=0):
    # Set the seed for random number generation
    random.seed(seed)
    
    # Initialize a Counter object to store the frequency of each letter
    letter_counter = Counter()
    
    # Iterate over each sublist in the list of lists
    for sublist in list_of_lists:
        # If the sublist is empty, fill it with a random sample from the alphabet
        if not sublist:
            sublist = [random.choice(ALPHABET) for _ in range(10)]  # Assuming we want 10 letters
        
        # Count the frequency of each letter in the sublist and update the letter_counter
        letter_counter.update(sublist)
    
    # Return the Counter object
    return letter_counter