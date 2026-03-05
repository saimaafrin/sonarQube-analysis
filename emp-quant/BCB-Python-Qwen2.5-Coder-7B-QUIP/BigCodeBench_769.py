
from collections import Counter
import itertools
import operator

def task_func(list_of_menuitems):
    # Flatten the list of menu items
    flattened_list = list(itertools.chain.from_iterable(list_of_menuitems))
    
    # Count the occurrences of each menu item
    menu_counts = Counter(flattened_list)
    
    # Find the most common menu item
    most_common_item = menu_counts.most_common(1)[0][0]
    
    # Return the most common menu item as a string
    return str(most_common_item)