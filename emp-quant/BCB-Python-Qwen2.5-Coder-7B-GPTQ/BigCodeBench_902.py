import pandas as pd
from collections import Counter
def task_func(d):
    # Initialize counters for each key
    x_counter = Counter()
    y_counter = Counter()
    z_counter = Counter()
    
    # Iterate through each dictionary in the list
    for item in d:
        # Update the counters based on the values of keys 'x', 'y', and 'z'
        if 'x' in item:
            x_counter[item['x']] += 1
        if 'y' in item:
            y_counter[item['y']] += 1
        if 'z' in item:
            z_counter[item['z']] += 1
    
    # Create a dictionary with the counters
    result = {
        'x': x_counter,
        'y': y_counter,
        'z': z_counter
    }
    
    return result