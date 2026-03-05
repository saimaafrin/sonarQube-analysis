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
        mu = np.mean(obj_list)
        std = np.std(obj_list)
    x = np.linspace(mu - 3 * std, mu + 3 * std, 100)
    y = stats.norm.pdf(x, mu, std)
    fig, ax = plt.subplots()
    ax.hist(obj_list, bins=50, density=True, alpha=0.5, label='Histogram')
    ax.plot(x, y, label='Custom normal distribution')
    ax.set_xlabel('Value')
    ax.set_ylabel('Frequency')
    ax.set_title('Histogram and custom normal distribution')
    ax.legend()
    return ax
obj_list = [ValueObject() for _ in range(10)]