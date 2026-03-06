
import pandas as pd
import numpy as np

def task_func(d):
    # Check if input is a list of dictionaries
    if not isinstance(d, list):
        raise ValueError("Input must be a list of dictionaries")

    # Create a DataFrame from the list of dictionaries
    df = pd.DataFrame(d)

    # Calculate mean, sum, max, min, and standard deviation for each key
    mean = df.mean()
    sum = df.sum()
    max = df.max()
    min = df.min()
    std = df.std()

    # Create a dictionary with the statistics
    stats = {'mean': mean, 'sum': sum, 'max': max, 'min': min, 'std': std}

    # Return the dictionary
    return stats