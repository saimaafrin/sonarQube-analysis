from collections import Counter
import itertools
import operator
def task_func(list_of_menuitems):
    """
    Flatten a nested list of menu items and return the most common menu item.
    """
    # Flatten the list of menu items
    flattened_list = itertools.chain.from_iterable(list_of_menuitems)

    # Count the frequency of each menu item
    menu_item_counts = Counter(flattened_list)

    # Get the most common menu item
    most_common_menu_item = menu_item_counts.most_common(1)[0][0]

    return most_common_menu_item
list_of_menuitems = [
    ['Apple', 'Orange', 'Banana'],
    ['Orange', 'Grape', 'Strawberry'],
    ['Banana', 'Mango', 'Pineapple']
]