
from collections import Counter
import random
from itertools import cycle
# Constants
ELEMENTS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
def task_func(l):
    # Move the first 3 elements to the end of the list
    l = l[3:] + l[:3]
    # Shuffle the list
    random.shuffle(l)
    # Create a frequency counter
    counter = Counter(l)
    return counter