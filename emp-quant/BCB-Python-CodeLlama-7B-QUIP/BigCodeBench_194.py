
import numpy as np
import matplotlib.pyplot as plt
# Constants
BAR_COLOR = ['blue', 'green', 'red', 'cyan', 'magenta', 'yellow', 'black']
def task_func(data_size):
    # Generate random data
    data = np.random.randint(1, 100, data_size)
    # Create histogram
    hist, edges = np.histogram(data, bins=50)
    # Select a random color
    color = np.random.choice(BAR_COLOR)
    # Plot the histogram
    plt.bar(edges[:-1], hist, color=color)
    plt.show()
    return data, color