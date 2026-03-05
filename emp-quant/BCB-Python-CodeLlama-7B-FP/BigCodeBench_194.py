import numpy as np
import matplotlib.pyplot as plt
BAR_COLOR = ['blue', 'green', 'red', 'cyan', 'magenta', 'yellow', 'black']
def task_func(data_size):
    # Generate random numeric data
    data = np.random.randint(0, 100, size=data_size)

    # Create histogram of the data
    plt.hist(data, color=np.random.choice(BAR_COLOR))

    # Return the array of randomly generated data and the color used for the histogram bars
    return data, plt.gca().get_facecolor()
data_size = 100