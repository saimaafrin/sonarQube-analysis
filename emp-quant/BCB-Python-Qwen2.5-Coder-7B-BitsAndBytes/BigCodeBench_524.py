
from collections import defaultdict
import numpy as np
import matplotlib.pyplot as plt

def task_func(data):
    # Check if the input data is empty
    if not data:
        raise ValueError("Input data cannot be empty")
    
    # Check if the input is a list of dictionaries
    if not all(isinstance(item, dict) for item in data):
        raise TypeError("Input must be a list of dictionaries")
    
    # Initialize a dictionary to store mean and standard deviation
    stats = defaultdict(lambda: {'mean': [], 'std': []})
    
    # Iterate over each dictionary in the list
    for d in data:
        for key, value in d.items():
            # Check if the value is numeric
            if not isinstance(value, (int, float)):
                raise TypeError(f"Value {value} for key {key} is not numeric")
            
            # Append the value to the respective list in the stats dictionary
            stats[key]['mean'].append(value)
            stats[key]['std'].append(value)
    
    # Calculate mean and standard deviation for each key
    results = {}
    axes_list = []
    
    for key, values in stats.items():
        mean_values = np.mean(values['mean'])
        std_values = np.std(values['std'])
        
        results[key] = {'mean': mean_values, 'std': std_values}
        
        # Create a bar chart for mean and standard deviation
        fig, ax = plt.subplots()
        ax.bar(['Mean', 'Standard Deviation'], [mean_values, std_values])
        ax.set_title(f'Mean and Standard Deviation for {key}')
        ax.set_ylabel('Values')
        axes_list.append(ax)
    
    return results, axes_list