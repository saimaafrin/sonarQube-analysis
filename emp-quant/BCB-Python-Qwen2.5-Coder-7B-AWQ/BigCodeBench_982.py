import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
def task_func(df, column, bins=30, density=True, alpha=0.6, color="g", seed=None):
    """
    Plots a histogram for a specified column of a pandas DataFrame and overlays it with a fitted normal distribution curve.
    
    Parameters:
    - df: pandas DataFrame containing the data.
    - column: String, the name of the column to plot.
    - bins: Integer, the number of bins in the histogram.
    - density: Boolean, whether to normalize the histogram.
    - alpha: Float, the transparency of the histogram and curve.
    - color: String, the color of the histogram and curve.
    - seed: Integer, the seed for the random number generator for reproducibility.
    
    Returns:
    - matplotlib.axes._axes.Axes: The matplotlib Axes object with the plot.
    """
    if seed is not None:
        np.random.seed(seed)
    
    # Extract the data from the specified column
    data = df[column].dropna()
    
    # Plot the histogram
    ax = data.plot(kind='hist', bins=bins, density=density, alpha=alpha, color=color, label='Histogram')
    
    # Fit a normal distribution to the data
    mu, std = norm.fit(data)
    
    # Plot the fitted normal distribution curve
    xmin, xmax = plt.xlim()
    x = np.linspace(xmin, xmax, 100)
    p = norm.pdf(x, mu, std)
    ax.plot(x, p, 'k', linewidth=2, label='Fitted Normal Distribution')
    
    # Add legend
    ax.legend()
    
    return ax