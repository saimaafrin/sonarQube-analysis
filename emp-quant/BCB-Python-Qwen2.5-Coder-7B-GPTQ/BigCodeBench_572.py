from random import randint
import matplotlib.pyplot as plt
import numpy as np
def task_func(array_length=100):
    # Generate two arrays of random integers
    array1 = np.array([randint(0, 100) for _ in range(array_length)])
    array2 = np.array([randint(0, 100) for _ in range(array_length)])
    
    # Calculate the maximum values of the respective elements of the two arrays
    max_values = np.maximum(array1, array2)
    
    # Create a line diagram with the maximum values
    fig, ax = plt.subplots()
    ax.plot(max_values, label='Maximum Values')
    
    # Set the y-axis label to 'Maximum Values'
    ax.set_ylabel('Maximum Values')
    
    # Add a legend to the plot
    ax.legend()
    
    return ax