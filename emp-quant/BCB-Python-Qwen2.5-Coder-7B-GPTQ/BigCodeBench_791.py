from collections import Counter
import random
from itertools import cycle
def task_func(l):
    # Ensure the list has at least 3 elements
    if len(l) < 3:
        raise ValueError("List must contain at least 3 elements")
    
    # Shuffle the list
    shuffled_list = random.sample(l, len(l))
    
    # Cycle through the shuffled list and take the first 3 elements
    first_three = next(cycle(shuffled_list))[:3]
    
    # Move the first 3 elements to the end of the list
    shuffled_list.extend(first_three)
    
    # Create a counter from the first 30 elements of the cycled, shuffled list
    counter = Counter(shuffled_list[:30])
    
    return counter