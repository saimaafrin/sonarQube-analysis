
import numpy as np
import matplotlib.pyplot as plt
# Constants
BAR_COLOR = ['blue', 'green', 'red', 'cyan', 'magenta', 'yellow', 'black']

def task_func(data_size):
    # Generate random numeric data
    data = np.random.rand(data_size)
    
    # Select a random color for the histogram bars
    color = np.random.choice(BAR_COLOR)
    
    # Create a histogram of the data
    plt.hist(data, color=color)
    plt.title(f'Histogram of Random Data with Color: {color}')
    plt.xlabel('Value')
    plt.ylabel('Frequency')
    plt.show()
    
    # Return the data array and the color used
    return data, color