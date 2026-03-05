
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
    # Generate values from ValueObjects
    values = [vo.value for vo in obj_list]
    
    # Calculate mean and standard deviation
    mean = np.mean(values)
    std = np.std(values)
    
    # Create a histogram
    fig, ax = plt.subplots()
    ax.hist(values, bins=30, density=True, alpha=0.6, color='g')
    
    # Draw a custom normal distribution curve
    x = np.linspace(mean - 3*std, mean + 3*std, 100)
    y = stats.norm.pdf(x, mean, std)
    ax.plot(x, y, 'r', linewidth=2)
    
    # Return the Axes
    return ax