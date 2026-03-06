
from collections import Counter
import itertools
import operator

def task_func(list_of_menuitems):
    # Flatten the nested list using itertools.chain.from_iterable
    flattened_list = list(itertools.chain.from_iterable(list_of_menuitems))
    
    # Count the occurrences of each menu item
    counter = Counter(flattened_list)
    
    # Find the most common menu item
    most_common_item, _ = counter.most_common(1)[0]
    
    return most_common_item