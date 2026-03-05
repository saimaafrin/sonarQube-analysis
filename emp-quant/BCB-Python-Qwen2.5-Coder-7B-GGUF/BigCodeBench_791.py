
from collections import Counter
import random
from itertools import cycle

# Constants
ELEMENTS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']

def task_func(l):
    # Ensure the list has at least 3 elements
    if len(l) < 3:
        raise ValueError("List must contain at least 3 elements")
    
    # Move the first 3 elements to the end of the list
    l = l[3:] + l[:3]
    
    # Shuffle the list
    random.shuffle(l)
    
    # Create a counter for the first 30 elements of the cycled, shuffled list
    counter = Counter(l[:30])
    
    return counter