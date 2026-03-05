import json
import numpy as np
from collections import defaultdict
import matplotlib.pyplot as plt
def task_func(input_file):
    # Read the JSON file
    with open(input_file, 'r') as f:
        data = json.load(f)

    # Create a dictionary to store the results
    results = defaultdict(dict)

    # Iterate over each key in the dictionaries
    for key in data[0].keys():
        # Extract the values for the current key
        values = [d[key] for d in data]

        # Calculate the mean and median of the values
        mean = np.mean(values)
        median = np.median(values)

        # Store the results in the dictionary
        results[key]['mean'] = mean
        results[key]['median'] = median

    # Create a list to store the plots
    plots = []

    # Iterate over each key in the dictionaries
    for key in data[0].keys():
        # Extract the values for the current key
        values = [d[key] for d in data]

        # Create a bar chart for the current key
        fig, ax = plt.subplots()
        ax.bar(values, label='Values')
        ax.set_title(f'{key} Mean and Median')
        ax.set_xlabel('Value')
        ax.set_ylabel('Count')
        ax.legend()
        plots.append(ax)

    # Return the results and plots
    return results, plots
input_file = 'data.json'