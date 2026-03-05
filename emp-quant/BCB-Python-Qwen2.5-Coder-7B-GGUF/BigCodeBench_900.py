
import pandas as pd
import numpy as np

def task_func(d):
    if not isinstance(d, list) or not all(isinstance(item, dict) for item in d):
        raise ValueError("Input must be a list of dictionaries.")
    
    stats = {}
    for key in ['x', 'y', 'z']:
        if key not in d[0]:
            raise ValueError(f"Key '{key}' not found in the dictionaries.")
        
        values = [item[key] for item in d]
        stats[key] = {
            'mean': np.mean(values),
            'sum': np.sum(values),
            'max': np.max(values),
            'min': np.min(values),
            'std': np.std(values)
        }
    
    return stats