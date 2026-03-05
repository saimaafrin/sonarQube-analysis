import numpy as np
import matplotlib.pyplot as plt
BAR_COLOR = ['blue', 'green', 'red', 'cyan', 'magenta', 'yellow', 'black']
def task_func(data_size):
    # Generate random data
    data = np.random.normal(size=data_size)
    # Create histogram
    plt.hist(data, color=np.random.choice(BAR_COLOR))
    # Return data and color used for histogram bars
    return data, plt.gca().get_facecolor()
data_size = 100