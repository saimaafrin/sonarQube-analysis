
from collections import Counter
import itertools
import operator

def task_func(list_of_menuitems):
    # Flatten the list of menu items
    flat_list = itertools.chain.from_iterable(list_of_menuitems)
    # Count the frequency of each menu item
    counter = Counter(flat_list)
    # Get the most common menu item
    most_common = counter.most_common(1)[0][0]
    return most_common