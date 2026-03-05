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
    
    # Calculate means and medians for each key
    for item in data:
        for key, value in item.items():
            means[key].append(value)
            medians[key].append(value)
    
    # Convert lists to numpy arrays for calculations
    means = {key: np.array(values) for key, values in means.items()}
    medians = {key: np.array(values) for key, values in medians.items()}
    
    # Calculate mean and median for each key
    result = {}
    plots = []
    for key in means:
        mean_value = np.mean(means[key])
        median_value = np.median(medians[key])
        result[key] = {'mean': mean_value, 'median': median_value}
        
        # Create bar chart for mean and median
        fig, ax = plt.subplots()
        ax.bar(['Mean', 'Median'], [mean_value, median_value], color=['blue', 'green'])
        ax.set_title(f'Mean and Median for {key}')
        ax.set_xlabel('Statistics')
        ax.set_ylabel('Values')
        plots.append(ax)
    
    return result, plots