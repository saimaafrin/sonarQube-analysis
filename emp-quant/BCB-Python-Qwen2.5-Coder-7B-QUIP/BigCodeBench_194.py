
import numpy as np
import matplotlib.pyplot as plt
# Constants
BAR_COLOR = ['blue', 'green', 'red', 'cyan', 'magenta', 'yellow', 'black']

def task_func(data_size):
    # Generate random data
    data = np.random.rand(data_size)
    
    # Select a random color for the histogram
    color = np.random.choice(BAR_COLOR)
    
    # Create the histogram
    plt.hist(data, bins=10, color=color)
    plt.show()
    
    # Return the data and the color
    return data, color