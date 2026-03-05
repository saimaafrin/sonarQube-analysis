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

    # Loop through each key in the dictionaries
    for key in data[0].keys():
        # Extract the values for the current key
        values = [d[key] for d in data]

        # Calculate the mean and median of the values
        mean = np.mean(values)
        median = np.median(values)

        # Store the results in the dictionary
        results[key]['mean'] = mean
        results[key]['median'] = median

    # Create a list of bar charts to visualize the results
    plots = []
    for key in results.keys():
        # Create a new figure and axis object
        fig, ax = plt.subplots()

        # Plot the mean and median values as a bar chart
        ax.bar(key, results[key]['mean'], label='Mean')
        ax.bar(key, results[key]['median'], label='Median')

        # Add a title and labels to the plot
        ax.set_title(f'{key} Mean and Median')
        ax.set_xlabel('Value')
        ax.set_ylabel('Count')
        ax.legend()

        # Add the plot to the list of plots
        plots.append(ax)

    # Return the results and plots
    return results, plots
input_file = 'data.json'