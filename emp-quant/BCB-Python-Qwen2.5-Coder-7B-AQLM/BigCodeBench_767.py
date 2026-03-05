
from collections import Counter
import random
import string

# Constants
LETTERS = string.ascii_letters

def task_func(list_of_lists):
    # Replace each sublist with a random letter
    random_letters = [random.choice(LETTERS) for _ in list_of_lists]
    
    # Count the occurrences of each letter
    letter_count = Counter(random_letters)
    
    return letter_count