
import numpy as np
import matplotlib.pyplot as plt
# Constants
BAR_COLOR = ['blue', 'green', 'red', 'cyan', 'magenta', 'yellow', 'black']
def task_func(data_size):
    # Generate random data
    data = np.random.randint(0, 100, size=data_size)
    # Create histogram
    plt.hist(data, color=np.random.choice(BAR_COLOR))
    # Get the color used for the histogram bars
    color = plt.gca().get_children()[0].get_facecolor()
    # Return the data and the color
    return data, color