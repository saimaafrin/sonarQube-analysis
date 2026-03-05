
import pandas as pd
import numpy as np

def task_func(d):
    if not isinstance(d, list) or not all(isinstance(i, dict) for i in d):
        raise ValueError("Input must be a list of dictionaries.")
    
    # Create a DataFrame from the list of dictionaries
    df = pd.DataFrame(d)
    
    # Calculate statistics for each key
    stats = {}
    for key in ['x', 'y', 'z']:
        if key in df.columns:
            stats[key] = {
                'mean': df[key].mean(),
                'sum': df[key].sum(),
                'max': df[key].max(),
                'min': df[key].min(),
                'std': df[key].std()
            }
    
    return stats

result = task_func(data)
print(result)