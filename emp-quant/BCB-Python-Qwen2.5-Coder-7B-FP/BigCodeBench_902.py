import pandas as pd
from collections import Counter
def task_func(d):
    # Initialize a dictionary to store the counters for 'x', 'y', and 'z'
    result = {'x': Counter(), 'y': Counter(), 'z': Counter()}
    
    # Iterate through each dictionary in the list
    for item in d:
        # Check if the key 'x' exists and update the counter
        if 'x' in item:
            result['x'].update([item['x']])
        # Check if the key 'y' exists and update the counter
        if 'y' in item:
            result['y'].update([item['y']])
        # Check if the key 'z' exists and update the counter
        if 'z' in item:
            result['z'].update([item['z']])
    
    return result