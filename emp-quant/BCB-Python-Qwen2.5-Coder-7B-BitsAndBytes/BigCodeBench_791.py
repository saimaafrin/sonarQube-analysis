
from collections import Counter
import random
from itertools import cycle

# Constants
ELEMENTS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']

def task_func(l):
    # Ensure the list has at least 3 elements
    if len(l) < 3:
        raise ValueError("List must contain at least 3 elements")
    
    # Shuffle the list
    random.shuffle(l)
    
    # Cycle through the list and take the first 30 elements
    cycled_list = list(islice(cycle(l), 30))
    
    # Move the first 3 elements to the end of the list
    moved_list = cycled_list[3:] + cycled_list[:3]
    
    # Create a counter for the first 30 elements of the moved list
    counter = Counter(moved_list)
    
    return counter