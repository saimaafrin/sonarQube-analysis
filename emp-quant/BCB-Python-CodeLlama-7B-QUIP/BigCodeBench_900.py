
import pandas as pd
import numpy as np

def task_func(d):
    # Check if input is a list of dictionaries
    if not all(isinstance(i, dict) for i in d):
        raise ValueError("Input must be a list of dictionaries")

    # Calculate statistics for keys 'x', 'y', and 'z'
    x = [i['x'] for i in d]
    y = [i['y'] for i in d]
    z = [i['z'] for i in d]
    mean_x = np.mean(x)
    mean_y = np.mean(y)
    mean_z = np.mean(z)
    sum_x = np.sum(x)
    sum_y = np.sum(y)
    sum_z = np.sum(z)
    max_x = np.max(x)
    max_y = np.max(y)
    max_z = np.max(z)
    min_x = np.min(x)
    min_y = np.min(y)
    min_z = np.min(z)
    std_x = np.std(x)
    std_y = np.std(y)
    std_z = np.std(z)

    # Create a dictionary with statistics
    stats = {
        'x': {
            'mean': mean_x,
            'sum': sum_x,
            'max': max_x,
            'min': min_x,
            'std': std_x
        },
        'y': {
            'mean': mean_y,
            'sum': sum_y,
            'max': max_y,
            'min': min_y,
            'std': std_y
        },
        'z': {
            'mean': mean_z,
            'sum': sum_z,
            'max': max_z,
            'min': min_z,
            'std': std_z
        }
    }

    return stats