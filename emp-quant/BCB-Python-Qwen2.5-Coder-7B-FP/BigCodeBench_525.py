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
    
    # Iterate over each key in the dictionaries
    for key in data[0].keys():
        values = [d[key] for d in data]
        values = np.array(values)
        
        # Calculate mean and median
        mean_value = np.mean(values)
        median_value = np.median(values)
        
        # Store the results
        result[key]['mean'] = mean_value
        result[key]['median'] = median_value
    
    # Initialize a list to store the plots
    plots = []
    
    # Create bar charts for mean and median
    for key in result.keys():
        fig, ax = plt.subplots()
        ax.bar(['Mean', 'Median'], [result[key]['mean'], result[key]['median']])
        ax.set_title(f'Mean and Median of {key}')
        ax.set_ylabel('Value')
        plots.append(ax)
    
    return result, plots