from collections import OrderedDict
from prettytable import PrettyTable
def task_func(my_dict):
    """
    Sorts a given dictionary by its keys in ascending order and returns a PrettyTable object displaying the sorted items with the names 'Key' and 'Value'.
    Display an empty dictionary.
    >>> str(task_func({})).startswith('+') True
    """
    # Sort the dictionary by its keys in ascending order
    sorted_dict = OrderedDict(sorted(my_dict.items(), key=lambda t: t[0]))

    # Create a PrettyTable object to display the sorted items
    table = PrettyTable()
    table.field_names = ["Key", "Value"]

    # Add the sorted items to the PrettyTable object
    for key, value in sorted_dict.items():
        table.add_row([key, value])

    # Return the PrettyTable object
    return table