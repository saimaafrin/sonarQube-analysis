
from collections import OrderedDict
from prettytable import PrettyTable

def task_func(my_dict):
    # Sort the dictionary by keys
    sorted_dict = OrderedDict(sorted(my_dict.items()))
    
    # Create a PrettyTable object
    table = PrettyTable(fieldnames=['Key', 'Value'])
    
    # Add sorted items to the table
    for key, value in sorted_dict.items():
        table.add_row([key, value])
    
    return table