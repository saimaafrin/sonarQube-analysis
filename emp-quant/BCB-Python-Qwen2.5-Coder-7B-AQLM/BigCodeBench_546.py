
from collections import OrderedDict
from prettytable import PrettyTable

def task_func(my_dict):
    # Sort the dictionary by keys
    sorted_dict = OrderedDict(sorted(my_dict.items()))
    
    # Create a PrettyTable object
    pt = PrettyTable()
    pt.field_names = ['Key', 'Value']
    
    # Add sorted items to the PrettyTable
    for key, value in sorted_dict.items():
        pt.add_row([key, value])
    
    return pt