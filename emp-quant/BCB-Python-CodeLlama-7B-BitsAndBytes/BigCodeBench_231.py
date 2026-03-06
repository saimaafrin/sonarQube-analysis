
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
import random
from matplotlib.axes import Axes

class ValueObject:
    value = 0
    def __init__(self, mu=0, std=1, seed=77):
        random.seed(seed)
        self.value = random.gauss(mu, std)

def task_func(obj_list):
    # Calculate the mean and standard deviation of the list of ValueObjects
    mu = np.mean([obj.value for obj in obj_list])
    std = np.std([obj.value for obj in obj_list])

    # Create a histogram of the values
    n, bins, patches = plt.hist(obj_list, bins=20, density=True)

    # Create a custom normal distribution curve
    x = np.linspace(mu - 3 * std, mu + 3 * std, 100)
    y = stats.norm.pdf(x, mu, std)

    # Plot the histogram and the custom normal distribution curve
    plt.plot(x, y, 'r--')
    plt.xlabel('Value')
    plt.ylabel('Frequency')
    plt.title('Histogram and Custom Normal Distribution Curve')

    # Return the plotted Axes
    return plt.gca()

# Show the plot
plt.show()