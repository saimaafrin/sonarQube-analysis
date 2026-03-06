
import pandas as pd
import numpy as np

def task_func(d):
    if not all(isinstance(item, dict) for item in d):
        raise ValueError("Input must be a list of dictionaries.")
    
    result = {}
    for key in ['x', 'y', 'z']:
        if any(key not in item for item in d):
            raise ValueError(f"All dictionaries must contain the key '{key}'.")
        
        values = [item[key] for item in d]
        stats = {
            'mean': np.mean(values),
            'sum': np.sum(values),
            'max': np.max(values),
            'min': np.min(values),
            'std_dev': np.std(values)
        }
        result[key] = stats
    
    return result