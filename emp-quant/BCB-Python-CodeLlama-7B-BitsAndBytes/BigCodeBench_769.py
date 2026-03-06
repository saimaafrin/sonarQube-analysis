
from collections import Counter
import itertools
import operator

def task_func(list_of_menuitems):
    # Flatten the list of menu items
    flattened_list = list(itertools.chain.from_iterable(list_of_menuitems))

    # Count the frequency of each menu item
    menu_item_counts = Counter(flattened_list)

    # Get the most common menu item
    most_common_menu_item = menu_item_counts.most_common(1)[0][0]

    return most_common_menu_item

print(task_func(list_of_menuitems))