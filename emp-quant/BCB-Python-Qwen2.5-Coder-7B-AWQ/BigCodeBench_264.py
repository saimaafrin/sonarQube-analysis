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
    data = np.random.normal(loc=value, scale=value, size=n)
    
    # Create a pandas Series from the generated data
    data_series = pd.Series(data)
    
    # Generate a histogram of the dataset
    plt.figure(figsize=(10, 6))
    plt.hist(data_series, bins=bins, edgecolor='black')
    plt.title(f'Histogram of Generated Data with Mean and Std Dev: {value}')
    plt.xlabel('Value')
    plt.ylabel('Frequency')
    plt.grid(True)
    plt.show()
    
    # Return the updated dictionary and the dataset as a pandas Series
    return dictionary, data_series