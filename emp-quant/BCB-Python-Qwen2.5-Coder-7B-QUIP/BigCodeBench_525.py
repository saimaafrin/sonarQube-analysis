
import json
import numpy as np
from collections import defaultdict
import matplotlib.pyplot as plt

def task_func(input_file):
    # Read the JSON file
    with open(input_file, 'r') as file:
        data = json.load(file)

    # Initialize dictionaries to store mean and median values
    mean_values = defaultdict(list)
    median_values = defaultdict(list)

    # Calculate mean and median for each key across all dictionaries
    for item in data:
        for key, value in item.items():
            mean_values[key].append(value)
            median_values[key].append(value)

    # Calculate mean and median for each key
    result = {}
    plots = []

    for key in mean_values:
        mean_value = np.mean(mean_values[key])
        median_value = np.median(median_values[key])
        result[key] = {'mean': mean_value, 'median': median_value}

        # Create bar charts for mean and median
        fig, ax = plt.subplots()
        ax.bar(['Mean', 'Median'], [mean_value, median_value], color=['blue', 'green'])
        ax.set_title(f'Bar Chart for {key}')
        ax.set_xlabel('Value Type')
        ax.set_ylabel('Value')
        plots.append(ax)

    return result, plots