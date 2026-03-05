
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
    
    # Create a figure and axis
    fig, ax = plt.subplots()
    
    # Plot the histogram
    ax.hist(values, bins=30, density=True, alpha=0.6, color='g')
    
    # Plot the custom normal distribution curve
   xmin, xmax = plt.xlim()
    x = np.linspace(xmin, xmax, 100)
    p = stats.norm.pdf(x, mean, std)
    ax.plot(x, p, 'k', linewidth=2)
    
    return ax