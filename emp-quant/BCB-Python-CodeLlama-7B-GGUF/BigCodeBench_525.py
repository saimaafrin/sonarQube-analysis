
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

            # Store the results in the dictionary
            results[k]['mean'] = mean
            results[k]['median'] = median

    # Create a list to store the plots
    plots = []

    # Iterate over the keys in the results dictionary
    for k, v in results.items():
        # Create a bar chart for the mean and median
        fig, ax = plt.subplots()
        ax.bar(x=['Mean', 'Median'], height=[v['mean'], v['median']])
        ax.set_title(k)
        ax.set_xlabel('Statistic')
        ax.set_ylabel('Value')
        plots.append(ax)

    # Return the results and plots
    return results, plots

# Print the results
print(results)

# Plot the results
for plot in plots:
    plot.show()