from collections import defaultdict
import numpy as np
import matplotlib.pyplot as plt
def task_func(data):
    if not data:
        raise ValueError("Input data is empty")
    
    if not all(isinstance(item, dict) for item in data):
        raise TypeError("Input is not a list of dictionaries")
    
    if not all(all(isinstance(value, (int, float)) for value in item.values()) for item in data):
        raise TypeError("All values in the dictionaries must be numeric")
    
    results = defaultdict(lambda: {'mean': [], 'std': []})
    
    for item in data:
        for key, value in item.items():
            results[key]['mean'].append(value)
            results[key]['std'].append(value)
    
    fig, axes = plt.subplots(len(results), 1, figsize=(10, 5*len(results)))
    
    for i, (key, values) in enumerate(results.items()):
        axes[i].bar(['Mean', 'Standard Deviation'], [np.mean(values['mean']), np.std(values['std'])])
        axes[i].set_title(f'Statistics for {key}')
        axes[i].set_ylabel('Values')
    
    plt.tight_layout()
    plt.show()
    
    return (results, axes)