
from collections import defaultdict
import numpy as np
import matplotlib.pyplot as plt

def task_func(data):
    if not data:
        raise ValueError("Input data is empty")
    
    if not isinstance(data, list) or not all(isinstance(item, dict) for item in data):
        raise TypeError("Input must be a list of dictionaries")
    
    results = defaultdict(list)
    for item in data:
        for key, value in item.items():
            if not isinstance(value, (int, float)):
                raise TypeError("All values in the dictionaries must be numeric")
            results[key].append(value)
    
    stats = {}
    axes = []
    for key, values in results.items():
        mean = np.mean(values)
        std_dev = np.std(values)
        stats[key] = (mean, std_dev)
        
        fig, ax = plt.subplots()
        ax.bar(['Mean', 'Standard Deviation'], [mean, std_dev], color=['blue', 'green'])
        ax.set_title(f'Statistics for {key}')
        ax.set_xlabel('Measure')
        ax.set_ylabel('Value')
        axes.append(ax)
    
    return stats, axes