
import json
import numpy as np
from collections import defaultdict
import matplotlib.pyplot as plt

def task_func(input_file):
    # Load the JSON file
    with open(input_file, 'r') as f:
        data = json.load(f)

    # Create a dictionary to store the results
    results = defaultdict(dict)

    # Iterate over each dictionary in the list
    for d in data:
        # Iterate over each key in the dictionary
        for k, v in d.items():
            # Calculate the mean and median of the values
            mean = np.mean(v)
            median = np.median(v)

            # Add the results to the results dictionary
            results[k]['mean'] = mean
            results[k]['median'] = median

    # Create a list to store the plots
    plots = []

    # Iterate over each key in the results dictionary
    for k, v in results.items():
        # Create a bar chart for the mean and median values
        fig, ax = plt.subplots()
        ax.bar(x=[0, 1], height=[v['mean'], v['median']], width=0.5)
        ax.set_title(f'{k} Mean and Median')
        ax.set_xlabel('Value')
        ax.set_ylabel('Count')
        ax.set_xticks([0, 1])
        ax.set_xticklabels(['Mean', 'Median'])
        plots.append(ax)

    # Return the results and plots
    return results, plots

# Print the results
print(results)

# Plot the results
for plot in plots:
    plot.show()