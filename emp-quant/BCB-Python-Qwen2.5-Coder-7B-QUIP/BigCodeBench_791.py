
from collections import Counter
import random
from itertools import cycle
# Constants
ELEMENTS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
def task_func(l):
    # Extend the list with its first 3 elements
    extended_list = l + l[:3]
    # Shuffle the extended list
    random.shuffle(extended_list)
    # Create a counter from the first 30 elements of the shuffled list
    counter = Counter(extended_list[:30])
    return counter