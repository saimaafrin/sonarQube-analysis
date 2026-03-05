import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats
def task_func(x, y, labels):
    """
    Draws normal distributions for multiple 'x' and 'y' arrays with labels.
    
    Parameters:
    x (list of arrays): List of x data arrays.
    y (list of arrays): List of y data arrays.
    labels (list of str): List of labels for each pair of x and y arrays.
    
    Returns:
    fig (Matplotlib figure object): The figure object containing the plots.
    """
    # Create a figure and axis
    fig, ax = plt.subplots()
    
    # Plot each normal distribution
    for i, (x_data, y_data, label) in enumerate(zip(x, y, labels)):
        # Fit a normal distribution to the data
        mu, std = stats.norm.fit(x_data)
        # Create a range of x values for the plot
        x_range = np.linspace(min(x_data), max(x_data), 100)
        # Calculate the y values for the normal distribution
        y_range = stats.norm.pdf(x_range, mu, std)
        # Plot the normal distribution
        ax.plot(x_range, y_range, label=f'{label} Normal Distribution')
    
    # Add labels and title
    ax.set_xlabel('X values')
    ax.set_ylabel('Probability Density')
    ax.set_title('Normal Distributions of Chemical Compounds')
    ax.legend()
    
    return fig