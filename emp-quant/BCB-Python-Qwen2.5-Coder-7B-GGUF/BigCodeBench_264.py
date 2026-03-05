
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def task_func(dictionary, key, value, n=100, bins=30, seed=0):
    # Check if the value is a number
    if not isinstance(value, (int, float)):
        raise ValueError("The provided value is not a number.")
    
    # Update the dictionary with the key-value pair
    dictionary[key] = value
    
    # Set the seed for reproducibility
    np.random.seed(seed)
    
    # Generate a random dataset following a normal distribution
    data = np.random.normal(dictionary[key], dictionary[key]/2, n)
    
    # Convert the dataset to a pandas Series
    data_series = pd.Series(data)
    
    # Generate a histogram of the dataset
    plt.hist(data_series, bins=bins, edgecolor='black')
    plt.title(f'Histogram of {key}')
    plt.xlabel('Value')
    plt.ylabel('Frequency')
    plt.show()
    
    # Return the updated dictionary and the dataset as a pandas Series
    return dictionary, data_series