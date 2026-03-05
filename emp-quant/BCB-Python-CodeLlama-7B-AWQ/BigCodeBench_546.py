from collections import OrderedDict
from prettytable import PrettyTable
def task_func(my_dict):
    """
    Sorts a given dictionary by its keys in ascending order and returns a PrettyTable object displaying the sorted items with the names 'Key' and 'Value'.
    """
    # Create an OrderedDict from the given dictionary
    od = OrderedDict(my_dict)

    # Create a PrettyTable object with the column headers
    pt = PrettyTable(['Key', 'Value'])

    # Add the sorted items to the PrettyTable object
    for key, value in od.items():
        pt.add_row([key, value])

    # Return the PrettyTable object
    return pt