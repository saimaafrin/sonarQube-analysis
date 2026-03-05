import json
import numpy as np
from collections import defaultdict
import matplotlib.pyplot as plt
def task_func(input_file):
    # Read the JSON file
    with open(input_file, 'r') as file:
        data = json.load(file)
    
    # Initialize dictionaries to store means and medians
    means = defaultdict(list)
    medians = defaultdict(list)
    
    # Calculate mean and median for each key across all dictionaries
    for item in data:
        for key, value in item.items():
            means[key].append(value)
            medians[key].append(value)
    
    # Convert lists to numpy arrays for calculation
    means = {key: np.array(values) for key, values in means.items()}
    medians = {key: np.array(values) for key, values in medians.items()}
    
    # Calculate mean and median
    mean_values = {key: np.mean(values) for key, values in means.items()}
    median_values = {key: np.median(values) for key, values in medians.items()}
    
    # Create a dictionary to store the results
    result = {key: {'mean': mean, 'median': median} for key, mean, median in zip(mean_values.keys(), mean_values.values(), median_values.values())}
    
    # Create bar charts for mean and median
    plots = []
    for key in mean_values.keys():
        fig, ax = plt.subplots()
        ax.bar(['Mean', 'Median'], [mean_values[key], median_values[key]])
        ax.set_title(f'Mean and Median for {key}')
        ax.set_xlabel('Statistics')
        ax.set_ylabel('Values')
        plots.append(ax)
    
    return result, plots