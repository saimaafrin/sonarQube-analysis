
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
    # Calculate the mean and standard deviation of the list
    mean = np.mean(obj_list)
    std = np.std(obj_list)

    # Plot the histogram and custom normal distribution curve
    fig, ax = plt.subplots()
    ax.hist(obj_list, bins=50, normed=True, facecolor='green', alpha=0.5, label='Histogram')
    x = np.linspace(min(obj_list), max(obj_list), 100)
    y = stats.norm.pdf(x, mean, std)
    ax.plot(x, y, 'r', label='Custom normal distribution curve')
    ax.set_xlabel('Value')
    ax.set_ylabel('Probability')
    ax.set_title('Histogram and custom normal distribution curve')
    ax.legend()
    return ax