import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
def task_func(size=1000):
    # Generate normally distributed random numbers
    data = np.random.normal(loc=0, scale=1, size=size)
    
    # Create a figure and axis for plotting
    fig, ax = plt.subplots()
    
    # Plot the histogram of the data
    ax.hist(data, bins=30, density=True, alpha=0.6, color='g')
    
    # Plot the probability density function of the normal distribution