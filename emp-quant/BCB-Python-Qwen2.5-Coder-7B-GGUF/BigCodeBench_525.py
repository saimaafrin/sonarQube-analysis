
import json
import numpy as np
from collections import defaultdict
import matplotlib.pyplot as plt

def task_func(input_file):
    # Read the JSON file
    with open(input_file, 'r') as file:
        data = json.load(file)
    
    # Initialize a dictionary to store the results
    result = defaultdict(dict)
    
    # Initialize a list to store the plots
    plots = []
    
    # Iterate over each key in the dictionaries
    for key in data[0].keys():
        values = [d[key] for d in data]
        values = np.array(values)
        
        # Calculate the mean and median
        mean_value = np.mean(values)
        median_value = np.median(values)
        
        # Store the results
        result[key]['mean'] = mean_value
        result[key]['median'] = median_value
        
        # Create a bar chart for the mean and median
        fig, ax = plt.subplots()
        ax.bar(['Mean', 'Median'], [mean_value, median_value])
        ax.set_title(f'Mean and Median of {key}')
        ax.set_xlabel('Statistics')
        ax.set_ylabel('Values')
        plots.append(ax)
    
    return result, plots