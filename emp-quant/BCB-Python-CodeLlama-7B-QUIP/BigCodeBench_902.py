
import pandas as pd
from collections import Counter

def task_func(d):
    # Create a dictionary to store the counts
    counts = {}

    # Loop through the list of dictionaries
    for i in range(len(d)):
        # Get the value for the key 'x'
        x_val = d[i]['x']
        # Check if the key 'x' exists in the counts dictionary
        if x_val in counts:
            # Increment the count for 'x'
            counts[x_val] += 1
        else:
            # Initialize the count for 'x' to 1
            counts[x_val] = 1

    # Loop through the list of dictionaries
    for i in range(len(d)):
        # Get the value for the key 'y'
        y_val = d[i]['y']
        # Check if the key 'y' exists in the counts dictionary
        if y_val in counts:
            # Increment the count for 'y'
            counts[y_val] += 1
        else:
            # Initialize the count for 'y' to 1
            counts[y_val] = 1

    # Loop through the list of dictionaries
    for i in range(len(d)):
        # Get the value for the key 'z'
        z_val = d[i]['z']
        # Check if the key 'z' exists in the counts dictionary
        if z_val in counts:
            # Increment the count for 'z'
            counts[z_val] += 1
        else:
            # Initialize the count for 'z' to 1
            counts[z_val] = 1

    # Return the counts dictionary
    return counts