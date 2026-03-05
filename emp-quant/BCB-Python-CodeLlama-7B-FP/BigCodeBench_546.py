from collections import OrderedDict
from prettytable import PrettyTable
def task_func(my_dict):
    """
    Sorts a given dictionary by its keys in ascending order and returns a PrettyTable object displaying the sorted items with the names 'Key' and 'Value'.
    """
    # Create an OrderedDict from the given dictionary
    od = OrderedDict(my_dict)

    # Sort the OrderedDict by its keys
    sorted_od = OrderedDict(sorted(od.items(), key=lambda t: t[0]))

    # Create a PrettyTable object to display the sorted items
    pt = PrettyTable()
    pt.field_names = ["Key", "Value"]

    # Add the sorted items to the PrettyTable object
    for key, value in sorted_od.items():
        pt.add_row([key, value])

    # Return the PrettyTable object
    return pt