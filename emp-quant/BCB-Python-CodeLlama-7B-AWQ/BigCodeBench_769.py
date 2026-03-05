from collections import Counter
import itertools
import operator
def task_func(list_of_menuitems):
    """
    Flattens a nested list of menu items and returns the most common menu item.
    """
    # Flatten the list of menu items
    flat_list = list(itertools.chain.from_iterable(list_of_menuitems))

    # Count the frequency of each menu item
    menu_item_counts = Counter(flat_list)

    # Get the most common menu item
    most_common_menu_item = menu_item_counts.most_common(1)[0][0]

    return most_common_menu_item