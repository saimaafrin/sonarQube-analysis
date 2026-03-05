from collections import Counter
import random
from itertools import cycle
def task_func(l):
    # Ensure the input list is not empty
    if not l:
        return Counter()
    
    # Cycle through the list and take the first 30 elements
    cycled_list = list(islice(cycle(l), 30))
    
    # Shuffle the first 3 elements to the end of the list
    cycled_list[3:] = cycled_list[3:] + cycled_list[:3]
    
    # Create a frequency counter for the modified list
    counter = Counter(cycled_list)
    
    return counter