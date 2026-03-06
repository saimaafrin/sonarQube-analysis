
import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt

def task_func(mean, std_dev, num_samples):
    # Generate samples from a normal distribution
    samples = np.random.normal(mean, std_dev, num_samples)
    
    # Create a figure and axis for plotting
    fig, ax = plt.subplots()
    
    # Plot the histogram of the samples
    n, bins, patches = ax.hist(samples, bins=30, density=True, alpha=0.6, color='g')
    
    # Calculate the PDF values for the range of x values
    xmin, xmax = plt.xlim()
    x = np.linspace(xmin, xmax, 100)
    p = norm.pdf(x, mean, std_dev)
    
    # Plot the PDF
    ax.plot(x, p, 'k', linewidth=2)
    
    # Set the title of the plot
    title = f"Fit results: mean = {mean:.2f}, std = {std_dev:.2f}"
    ax.set_title(title)
    
    # Return the figure and the samples
    return fig, samples