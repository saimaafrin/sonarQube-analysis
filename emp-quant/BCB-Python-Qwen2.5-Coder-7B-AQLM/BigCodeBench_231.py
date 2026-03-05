
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
    if not obj_list:
        mean = 0
        std = 0
    else:
        values = [obj.value for obj in obj_list]
        mean = np.mean(values)
        std = np.std(values)
    
    # Create a histogram of the values
    plt.figure()
    plt.hist(values, bins=30, density=True, alpha=0.6, color='g')
    
    # Create a custom normal distribution curve
    xmin, xmax = plt.xlim()
    x = np.linspace(xmin, xmax, 100)
    p = stats.norm.pdf(x, mean, std)
    plt.plot(x, p, 'k', linewidth=2)
    
    # Return the plotted Axes
    return plt.gca()