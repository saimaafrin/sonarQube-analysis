
from collections import OrderedDict
from prettytable import PrettyTable

def task_func(my_dict):
    # Sort the dictionary by its keys in ascending order
    sorted_dict = OrderedDict(sorted(my_dict.items(), key=lambda x: x[0]))

    # Create a PrettyTable object to display the sorted items
    table = PrettyTable()
    table.field_names = ["Key", "Value"]

    # Add the sorted items to the table
    for key, value in sorted_dict.items():
        table.add_row([key, value])

    # Return the PrettyTable object
    return table