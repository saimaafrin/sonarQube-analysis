import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt
def task_func(mean, std_dev, num_samples):
    """
    Generates a histogram of samples drawn from a normal distribution and overlays the probability density function (PDF) of the normal distribution. The plot is titled with the fit results, showing the mean and standard deviation used in the generation. The function returns both the plot and the samples generated.
    
    Parameters:
    - mean (float): The mean of the normal distribution.
    - std_dev (float): The standard deviation of the normal distribution.
    - num_samples (int): The number of samples to draw from the distribution.
    
    Returns:
    - tuple: A tuple containing:
        - matplotlib.figure.Figure: The figure object for the plot.
        - numpy.ndarray: An array of samples drawn from the normal distribution.
    """
    # Generate samples from the normal distribution
    samples = np.random.normal(mean, std_dev, num_samples)
    
    # Create a figure and axis for the plot
    fig, ax = plt.subplots()
    
    # Plot the histogram of the samples
    n, bins, patches = ax.hist(samples, bins=30, density=True, alpha=0.6, color='g')
    
    # Plot the PDF of the normal distribution
    xmin, xmax = plt.xlim()
    x = np.linspace(xmin, xmax, 100)
    p = norm.pdf(x, mean, std_dev)
    ax.plot(x, p, 'k', linewidth=2)
    
    # Set the title of the plot
    title = f"Fit results: mean = {mean:.2f}, std = {std_dev:.2f}"
    ax.set_title(title)
    
    # Return the figure and the samples
    return fig, samples