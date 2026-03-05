
from itertools import groupby
from operator import itemgetter
# Constants
KEY_FUNC = itemgetter(0)

def task_func(my_dict):
    # Sort the dictionary items by the first character of the key
    sorted_items = sorted(my_dict.items(), key=KEY_FUNC)
    
    # Group the items by the first character of the key
    grouped_items = groupby(sorted_items, key=KEY_FUNC)
    
    # Aggregate the values for each group
    aggregated_dict = {}
    for key, group in grouped_items:
        aggregated_dict[key] = sum(item[1] for item in group)
    
    return aggregated_dict