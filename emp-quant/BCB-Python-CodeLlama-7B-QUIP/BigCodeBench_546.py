
from collections import OrderedDict
from prettytable import PrettyTable

def task_func(my_dict):
    # Sort the dictionary by its keys in ascending order
    sorted_dict = OrderedDict(sorted(my_dict.items(), key=lambda x: x[0]))

    # Create a PrettyTable object to display the sorted items
    table = PrettyTable()
    table.add_column("Key", [key for key, value in sorted_dict])
    table.add_column("Value", [value for key, value in sorted_dict])

    return table