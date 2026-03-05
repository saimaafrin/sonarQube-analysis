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

    # Iterate over the dictionaries in the list
    for d in data:
        # Iterate over the keys in each dictionary
        for k, v in d.items():
            # Calculate the mean and median of the values
            mean = np.mean(v)
            median = np.median(v)

            # Add the results to the results dictionary
            results[k]['mean'] = mean
            results[k]['median'] = median

    # Create a list of bar charts
    plots = []

    # Iterate over the keys in the results dictionary
    for k, v in results.items():
        # Create a bar chart for each key
        ax = plt.subplot()
        ax.bar(v['mean'], v['median'])
        ax.set_title(f'Mean and Median of {k}')
        ax.set_xlabel('Value')
        ax.set_ylabel('Count')
        plots.append(ax)

    # Return the results and the plots
    return results, plots
input_file = 'data.json'