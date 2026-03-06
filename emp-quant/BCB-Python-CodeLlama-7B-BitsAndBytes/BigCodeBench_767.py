
from collections import Counter
import random
import string

# Constants
LETTERS = string.ascii_letters

def task_func(list_of_lists):
    # Replace each sublist with a random letter
    new_list = [random.choice(LETTERS) for sublist in list_of_lists]

    # Count the letters in the final list
    letter_counts = Counter(new_list)

    return letter_counts