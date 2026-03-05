
import pandas as pd
from collections import Counter

def task_func(d):
    # Create a dictionary to store the counts
    counts = {'x': Counter(), 'y': Counter(), 'z': Counter()}

    # Iterate over the list of dictionaries
    for item in d:
        # Extract the values for 'x', 'y', and 'z'
        x_val = item.get('x')
        y_val = item.get('y')
        z_val = item.get('z')

        # Increment the counts for each value
        counts['x'][x_val] += 1
        counts['y'][y_val] += 1
        counts['z'][z_val] += 1

    return counts