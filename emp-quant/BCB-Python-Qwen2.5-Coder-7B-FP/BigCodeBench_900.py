import pandas as pd
import numpy as np
def task_func(d):
    # Check if the input is a list of dictionaries
    if not isinstance(d, list) or not all(isinstance(item, dict) for item in d):
        raise ValueError("Input must be a list of dictionaries.")
    
    # Extract the values for keys 'x', 'y', and 'z'
    x_values = [item['x'] for item in d]
    y_values = [item['y'] for item in d]
    z_values = [item['z'] for item in d]
    
    # Calculate statistics for each key
    x_stats = {'mean': np.mean(x_values), 'sum': np.sum(x_values), 'max': np.max(x_values), 'min': np.min(x_values), 'std': np.std(x_values)}
    y_stats = {'mean': np.mean(y_values), 'sum': np.sum(y_values), 'max': np.max(y_values), 'min': np.min(y_values), 'std': np.std(y_values)}
    z_stats = {'mean': np.mean(z_values), 'sum': np.sum(z_values), 'max': np.max(z_values), 'min': np.min(z_values), 'std': np.std(z_values)}
    
    # Return the result as a dictionary
    return {'x': x_stats, 'y': y_stats, 'z': z_stats}