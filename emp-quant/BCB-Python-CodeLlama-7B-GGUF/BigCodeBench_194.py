
import numpy as np
import matplotlib.pyplot as plt
# Constants
BAR_COLOR = ['blue', 'green', 'red', 'cyan', 'magenta', 'yellow', 'black']
def task_func(data_size):
    # Generate random data
    data = np.random.normal(size=data_size)
    # Create histogram
    plt.hist(data, color=np.random.choice(BAR_COLOR))
    # Set title and labels
    plt.title('Random Data Histogram')
    plt.xlabel('Value')
    plt.ylabel('Frequency')
    # Show plot
    plt.show()
    # Return data and color
    return data, np.random.choice(BAR_COLOR)