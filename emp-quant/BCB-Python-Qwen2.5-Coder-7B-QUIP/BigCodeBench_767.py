
from collections import Counter
import random
import string
# Constants
LETTERS = string.ascii_letters

def task_func(list_of_lists):
    # Replace each sublist with a random letter
    random_letters = [random.choice(LETTERS) for _ in range(len(list_of_lists))]
    
    # Flatten the list of lists and count the occurrences of each letter
    flattened_list = [letter for sublist in list_of_lists for letter in sublist]
    letter_counts = Counter(flattened_list)
    
    # Return the count of each letter as a dictionary
    return dict(letter_counts)