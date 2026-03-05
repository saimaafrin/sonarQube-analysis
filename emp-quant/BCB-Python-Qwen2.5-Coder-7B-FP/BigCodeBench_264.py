import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
def task_func(dictionary, key, value, n=100, bins=30, seed=0):
    # Check if the value is a number
    if not isinstance(value, (int, float)):
        raise ValueError("The provided value is not a number.")
    
    # Update the dictionary with the key-value pair
    dictionary[key] = value
    
    # Set the random seed for reproducibility
    np.random.seed(seed)
    
    # Generate a random dataset following a normal distribution
    dataset = pd.Series(np.random.normal(dictionary[key], dictionary[key]/2, n))
    
    # Plot a histogram of the generated dataset
    plt.figure(figsize=(10, 6))
    dataset.plot(kind='hist', bins=bins, edgecolor='black')
    plt.title(f'Histogram of Dataset with Mean and Std Dev: {dictionary[key]}')
    plt.xlabel('Value')
    plt.ylabel('Frequency')
    plt.show()
    
    # Return the updated dictionary and the dataset
    return dictionary, dataset