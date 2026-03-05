from collections import defaultdict
import numpy as np
import matplotlib.pyplot as plt
def task_func(data):
    if not data:
        raise ValueError("Input data is empty")
    
    if not all(isinstance(item, dict) for item in data):
        raise TypeError("Input is not a list of dictionaries")
    
    if not all(all(isinstance(value, (int, float)) for value in item.values()) for item in data):
        raise TypeError("All values in the dictionaries are not numeric")
    
    results = defaultdict(list)
    for item in data:
        for key, value in item.items():
            results[key].append(value)
    
    stats = {}
    axes = []
    for key, values in results.items():
        mean = np.mean(values)
        std_dev = np.std(values)
        stats[key] = (mean, std_dev)
        
        fig, ax = plt.subplots()
        ax.bar(['Mean', 'Standard Deviation'], [mean, std_dev])
        ax.set_title(f'Statistics for {key}')
        axes.append(ax)
    
    return stats, axes