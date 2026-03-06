from collections import OrderedDict
from prettytable import PrettyTable
def task_func(my_dict):
    """
    Sorts a given dictionary by its keys in ascending order and returns a PrettyTable object displaying the sorted items with the names 'Key' and 'Value'.

    Parameters:
    my_dict (dict): The dictionary to be sorted and displayed.

    Returns:
    PrettyTable: A PrettyTable object representing the sorted dictionary.

    Requirements:
    - collections.OrderedDict
    - prettytable.PrettyTable

    Examples:
    Display a simple dictionary in a sorted table format.
    >>> table = task_func({3: 'apple', 1: 'banana', 2: 'cherry'})
    >>> str(table).startswith('+') and 'banana' in str(table)
    True

    Display an empty dictionary.
    >>> str(task_func({})).startswith('+')
    True
    """
    if not isinstance(my_dict, dict):
        raise TypeError('The given argument is not a dictionary.')
    if not my_dict:
        return PrettyTable()
    sorted_dict = OrderedDict(sorted(my_dict.items()))
    table = PrettyTable()
    table.field_names = ['Key', 'Value']
    for key, value in sorted_dict.items():
        table.add_row([key, value])
    return table