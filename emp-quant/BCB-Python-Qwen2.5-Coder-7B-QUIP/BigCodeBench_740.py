
from collections import Counter
import heapq
# Constants
LETTERS = list('abcdefghijklmnopqrstuvwxyz')

def task_func(my_dict):
    # Initialize a counter with the dictionary values
    letter_counter = Counter(my_dict)
    
    # Get the 3 most common letters
    most_common_letters = letter_counter.most_common(3)
    
    # Extract just the letters from the list of tuples
    most_common_letters = [item[0] for item in most_common_letters]
    
    return most_common_letters