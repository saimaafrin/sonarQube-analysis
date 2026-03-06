
import collections
import numpy as np

def task_func(file_name):
    # Open the CSV file
    with open(file_name, 'r') as f:
        # Skip the header row
        next(f)
        # Create a dictionary to store the most common values for each column
        col_vals = collections.defaultdict(list)
        # Read the CSV file and store the values in the dictionary
        for line in f:
            values = line.strip().split(',')
            for i, val in enumerate(values):
                col_vals[i].append(val)
        # Find the most common value for each column
        most_common = {}
        for col, vals in col_vals.items():
            if vals:
                most_common[col] = max(set(vals), key=vals.count)
            else:
                most_common[col] = None
    return most_common