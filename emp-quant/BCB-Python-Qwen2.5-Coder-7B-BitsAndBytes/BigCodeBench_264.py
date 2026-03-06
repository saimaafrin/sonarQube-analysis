
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def task_func(dictionary, key, value, n=100, bins=30, seed=0):
    if not isinstance(value, (int, float)):
        raise ValueError("The provided value must be a number.")
    
    dictionary[key] = value
    
    np.random.seed(seed)
    data = np.random.normal(loc=value, scale=value/2, size=n)  # Assuming std dev is half of the mean
    series_data = pd.Series(data)
    
    plt.figure(figsize=(8, 6))
    series_data.plot(kind='hist', bins=bins, edgecolor='black')
    plt.title(f'Histogram of {key} Dataset')
    plt.xlabel(key)
    plt.ylabel('Frequency')
    plt.show()
    
    return dictionary, series_data