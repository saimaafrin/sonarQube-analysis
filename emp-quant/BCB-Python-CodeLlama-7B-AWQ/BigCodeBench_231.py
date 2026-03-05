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
def task_func(obj_list) -> Axes:
    """
    Draw the histogram and the custom normal distribution curve from the mean and standard deviation derived from the values of a list of ValueObjects and return the plotted Axes.
    For an empty list, the mean and the standard deviation is 0.
    """
    if not obj_list:
        mu = 0
        std = 0
    else:
        values = [obj.value for obj in obj_list]
        mu = np.mean(values)
        std = np.std(values)

    # Plot the histogram
    n, bins, patches = plt.hist(values, bins='auto', alpha=0.5, label='Histogram')

    # Plot the custom normal distribution curve
    x = np.linspace(mu - 3 * std, mu + 3 * std, 100)
    y = stats.norm.pdf(x, mu, std)
    plt.plot(x, y, label='Custom normal distribution')

    # Add axis labels and title
    plt.xlabel('Value')
    plt.ylabel('Frequency')
    plt.title('Histogram and Custom Normal Distribution')
    plt.legend()

    return plt.gca()
obj_list = [ValueObject() for _ in range(10)]