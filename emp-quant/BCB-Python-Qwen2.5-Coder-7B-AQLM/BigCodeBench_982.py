
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

def task_func(df, column, bins=30, density=True, alpha=0.6, color="g", seed=None):
    """
    Plots a histogram for a specified column of a pandas DataFrame and overlays it with a fitted normal distribution curve.
    
    Parameters:
    - df (pandas.DataFrame): The DataFrame containing the data.
    - column (str): The name of the column to plot.
    - bins (int): The number of bins in the histogram.
    - density (bool): If True, the histogram is normalized to form a probability density.
    - alpha (float): The transparency of the histogram.
    - color (str): The color of the histogram.
    - seed (int): The seed for the random number generator for reproducibility.
    
    Returns:
    - matplotlib.axes._axes.Axes: The matplotlib Axes object with the plot.
    """
    if seed is not None:
        np.random.seed(seed)
    
    # Extract the data from the specified column
    data = df[column].dropna()
    
    # Plot the histogram
    ax = data.hist(bins=bins, density=density, alpha=alpha, color=color)
    
    # Fit a normal distribution to the data
    mu, std = norm.fit(data)
    
    # Plot the normal distribution curve
    xmin, xmax = plt.xlim()
    x = np.linspace(xmin, xmax, 100)
    p = norm.pdf(x, mu, std)
    ax.plot(x, p, 'k', linewidth=2)
    
    # Add a legend
    ax.legend(['Normal fit', 'Histogram'], loc='best')
    
    return ax