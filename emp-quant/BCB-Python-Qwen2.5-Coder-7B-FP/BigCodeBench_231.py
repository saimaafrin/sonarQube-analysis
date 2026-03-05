import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
import random
from matplotlib.axes import Axes
def task_func(obj_list) -> Axes:
    # Calculate mean and standard deviation from the list of ValueObjects
    if not obj_list:
        mean = 0
        std = 0
    else:
        values = [obj.value for obj in obj_list]
        mean = np.mean(values)
        std = np.std(values)
    
    # Generate a range of x values for the normal distribution curve
    x = np.linspace(mean - 3*std, mean + 3*std, 100)
    
    # Calculate the y values for the normal distribution curve
    y = stats.norm.pdf(x, mean, std)
    
    # Create a figure and an axes object
    fig, ax = plt.subplots()
    
    # Plot the histogram of the values
    ax.hist(values, bins=30, density=True, alpha=0.6, color='g')
    
    # Plot the custom normal distribution curve
    ax.plot(x, y, 'r-', lw=2)
    
    # Set the title and labels
    ax.set_title('Histogram and Normal Distribution Curve')
    ax.set_xlabel('Value')
    ax.set_ylabel('Probability Density')
    
    # Return the axes object
    return ax