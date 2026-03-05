from collections import Counter
import random
from itertools import cycle
ELEMENTS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
def task_func(l):
    """
    Create a counter from a list "l" and move the first 3 elements to the end of the list.
    """
    # Move the first 3 elements to the end of the list
    l.extend(l[:3])
    l = l[3:]

    # Create a frequency counter
    counter = Counter(l)

    # Test the counter
    assert counter['A'] == 1
    assert counter['B'] == 1
    assert counter['C'] == 1
    assert counter['D'] == 1
    assert counter['E'] == 1
    assert counter['F'] == 1
    assert counter['G'] == 1
    assert counter['H'] == 1
    assert counter['I'] == 1
    assert counter['J'] == 1

    return counter
l = ELEMENTS