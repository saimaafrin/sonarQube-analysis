
import json
import numpy as np
from collections import defaultdict
import matplotlib.pyplot as plt

def task_func(input_file):
    # Read the JSON file
    with open(input_file, 'r') as file:
        data = json.load(file)
    
    # Initialize a dictionary to store the means and medians
    stats = defaultdict(dict)
    
    # Calculate mean and median for each key
    for item in data:
        for key, value in item.items():
            if key not in stats:
                stats[key]['values'] = []
            stats[key]['values'].append(value)
    
    for key, values in stats.items():
        values_array = np.array(values['values'])
        stats[key]['mean'] = np.mean(values_array)
        stats[key]['median'] = np.median(values_array)
    
    # Create bar charts for mean and median
    plots = []
    fig, axes = plt.subplots(len(stats), 2, figsize=(10, len(stats) * 4))
    
    for i, (key, values) in enumerate(stats.items()):
        ax_mean = axes[i, 0]
        ax_median = axes[i, 1]
        
        ax_mean.bar(['Mean'], [values['mean']], color='blue')
        ax_mean.set_title(f'Mean of {key}')
        ax_mean.set_ylabel('Value')
        
        ax_median.bar(['Median'], [values['median']], color='green')
        ax_median.set_title(f'Median of {key}')
        ax_median.set_ylabel('Value')
    
    plt.tight_layout()
    plt.show()
    
    return stats, plots