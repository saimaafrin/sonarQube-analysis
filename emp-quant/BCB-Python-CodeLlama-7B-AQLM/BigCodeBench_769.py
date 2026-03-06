from collections import Counter
import itertools
import operator
def task_func(list_of_menuitems):
    """
    Faced with a nested list of menu items, flatten the list and return the most common menu item.

    Parameters:
    - list_of_menuitems (list): A nested list of menu items.

    Returns:
    - str: The most common menu item.

    Requirements:
    - collections
    - itertools
    - operator

    Example:
    >>> task_func([['Pizza', 'Burger'], ['Pizza', 'Coke'], ['Pasta', 'Coke']])
    'Pizza'
    """
    # Your code here
    flattened_list = [item for sublist in list_of_menuitems for item in sublist]
    counter = Counter(flattened_list)
    most_common = counter.most_common(1)
    return most_common[0][0]