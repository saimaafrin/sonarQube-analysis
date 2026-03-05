
import pandas as pd
import numpy as np

def task_func(d):
    if not isinstance(d, list) or not all(isinstance(item, dict) for item in d):
        raise ValueError("Input must be a list of dictionaries.")
    
    stats_dict = {}
    for key in ['x', 'y', 'z']:
        values = [item[key] for item in d if key in item]
        if values:
            stats_dict[key] = {
                'mean': np.mean(values),
                'sum': np.sum(values),
                'max': np.max(values),
                'min': np.min(values),
                'std': np.std(values)
            }
        else:
            stats_dict[key] = {
                'mean': None,
                'sum': None,
                'max': None,
                'min': None,
                'std': None
            }
    
    return stats_dict