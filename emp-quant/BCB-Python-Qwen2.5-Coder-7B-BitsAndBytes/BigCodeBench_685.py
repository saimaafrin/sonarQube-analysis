
from collections import Counter
from itertools import chain

def task_func(list_of_lists):
    # Merge all sublists into one list using chain.from_iterable
    merged_list = list(chain.from_iterable(list_of_lists))
    
    # Create a Counter object to count occurrences of each element
    element_count = Counter(merged_list)
    
    return element_count