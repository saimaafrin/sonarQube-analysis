
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
        mean_val = 0
        std_dev = 0
    else:
        values = [obj.value for obj in obj_list]
        mean_val = np.mean(values)
        std_dev = np.std(values)
    
    # Create a figure and axis
    fig, ax = plt.subplots()
    
    # Plot the histogram
    ax.hist(values, bins=30, density=True, alpha=0.6, color='g')
    
    # Define the range for the normal distribution curve
    x = np.linspace(mean_val - 4*std_dev, mean_val + 4*std_dev, 100)
    
    # Calculate the normal distribution curve
    y = stats.norm.pdf(x, mean_val, std_dev)
    
    # Plot the normal distribution curve
    ax.plot(x, y, 'r-', lw=2)
    
    return ax