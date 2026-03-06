import numpy as np
import matplotlib.pyplot as plt
from statsmodels.formula.api import ols
def task_func(mu, sigma, seed=0, num_samples=1000, num_bins=30):
    '''
    Create a histogram of a normal distribution with a given mean and standard deviation, and overlay the 
    probability density function (PDF) of the normal distribution on the histogram. Additionally, overlay a 
    second order polynomial function on the histogram fitted bin-wise using ordinary least squares (OLS) 
    regression. The random seed is set for reproducibility. The color of the PDF line is red, and the color of the OLS line is green.
    
    Parameters:
    - mu (float): The mean of the distribution.
    - sigma (float): The standard deviation of the distribution.
    - seed (int, Optional): The random seed for reproducibility. Defaults to 0.
    - num_samples (int, Optional): The number of samples to generate from the distribution. Defaults to 1000.
    - num_bins (int, Optional): The number of bins to use in the histogram. Defaults to 30.
    
    Returns:
    - matplotlib.axes.Axes: The Axes object with the histogram and overlaid PDF.
    
    Requirements:
    - numpy
    - matplotlib.pyplot
    - statsmodels.formula.api
    
    Example:
    >>> ax = task_func(0, 1)
    >>> type(ax)
    <class 'matplotlib.axes._axes.Axes'>
    '''
    np.random.seed(seed)
    x = np.random.normal(mu, sigma, num_samples)
    ax = plt.hist(x, bins=num_bins, density=True, color='#000000')
    ax = plt.plot(ax[1][1:], np.poly1d(np.polyfit(ax[1][1:], ax[0], 2))(ax[1][1:]), color='#00FF00')
    ax = plt.plot(ax[1][1:], np.exp(-0.5 * ((ax[1][1:] - mu) / sigma) ** 2) / np.sqrt(2 * np.pi) / sigma, color='#FF0000')
    return ax