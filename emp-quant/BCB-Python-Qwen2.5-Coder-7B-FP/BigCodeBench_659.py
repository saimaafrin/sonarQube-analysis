import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats
def task_func(x, y, labels):
    """
    Draws normal distributions for multiple 'x' and 'y' arrays with labels.
    
    Parameters:
    x (list of np.ndarray): List of x data arrays.
    y (list of np.ndarray): List of y data arrays.
    labels (list of str): List of labels for each data pair.
    
    Returns:
    fig (matplotlib.figure.Figure): Matplotlib figure object.
    """
    # Create a figure and axis
    fig, ax = plt.subplots()
    
    # Plot each normal distribution
    for xi, yi, label in zip(x, y, labels):
        # Fit a normal distribution to the data
        mu, std = stats.norm.fit(xi)
        # Plot the normal distribution
        xmin, xmax = plt.xlim()
        x = np.linspace(xmin, xmax, 100)
        p = stats.norm.pdf(x, mu, std)
        ax.plot(x, p, label=label)
    
    # Add labels and legend
    ax.set_xlabel('X')
    ax.set_ylabel('Probability Density')
    ax.legend()
    
    return fig