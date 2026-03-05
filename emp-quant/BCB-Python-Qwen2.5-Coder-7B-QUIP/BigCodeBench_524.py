
from collections import defaultdict
import numpy as np
import matplotlib.pyplot as plt

def task_func(data):
    if not data:
        raise ValueError("Input data is empty")
    
    if not isinstance(data, list):
        raise TypeError("Input must be a list of dictionaries")
    
    if not all(isinstance(item, dict) for item in data):
        raise TypeError("All items in the list must be dictionaries")
    
    results = defaultdict(lambda: {'mean': [], 'std': []})
    axes = []
    
    for item in data:
        for key, value in item.items():
            if not isinstance(value, (int, float)):
                raise TypeError("All values in the dictionaries must be numeric")
            results[key]['mean'].append(value)
            results[key]['std'].append(0)  # Standard deviation is 0 for single values
    
    for key, result in results.items():
        result['mean'] = np.mean(result['mean'])
        result['std'] = np.std(result['std'])
    
    fig, axs = plt.subplots(len(results), 1, figsize=(10, len(results) * 2))
    if len(results) == 1:
        axs = [axs]
    
    for i, (key, result) in enumerate(results.items()):
        axs[i].bar(key, result['mean'], yerr=result['std'], capsize=5)
        axs[i].set_title(f'{key} Mean and Std Dev')
        axs[i].set_xlabel('Key')
        axs[i].set_ylabel('Value')
    
    plt.tight_layout()
    plt.show()
    
    return (results, axs)