import pandas as pd
from collections import Counter
def task_func(d):
    # Initialize a dictionary to store the counters for 'x', 'y', and 'z'
    result = {'x': Counter(), 'y': Counter(), 'z': Counter()}
    
    # Iterate through each dictionary in the list
    for item in d:
        # Check if the key exists in the dictionary and update the corresponding counter
        if 'x' in item:
            result['x'].update([item['x']])
        if 'y' in item:
            result['y'].update([item['y']])
        if 'z' in item:
            result['z'].update([item['z']])
    
    return result