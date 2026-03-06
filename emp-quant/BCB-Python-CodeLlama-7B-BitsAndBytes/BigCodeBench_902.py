
import pandas as pd
from collections import Counter

def task_func(d):
    # Create a dictionary to store the counts
    counts = {}

    # Iterate over the dictionaries in the list
    for item in d:
        # Extract the values for the keys 'x', 'y', and 'z'
        x_val = item.get('x', None)
        y_val = item.get('y', None)
        z_val = item.get('z', None)

        # Increment the counts for each value
        if x_val is not None:
            counts['x'] += 1
        if y_val is not None:
            counts['y'] += 1
        if z_val is not None:
            counts['z'] += 1

    # Return the counts as a dictionary
    return counts

print(task_func(d))