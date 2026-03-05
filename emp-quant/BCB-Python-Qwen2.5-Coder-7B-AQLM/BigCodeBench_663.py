
import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

def task_func(x, y, labels):
    """
    Fits an exponential curve to given data points and plots the curves with labels.
    
    Parameters:
    x (list of lists): A list of x data points for each set of data.
    y (list of lists): A list of y data points for each set of data.
    labels (list of str): A list of labels for each set of data.
    
    Returns:
    matplotlib.figure.Figure: The figure object that contains the plotted curves.
    """
    def exponential_func(x, a, b, c):
        return a * np.exp(-b * x) + c
    
    fig, ax = plt.subplots()
    
    for xi, yi, label in zip(x, y, labels):
        popt, _ = curve_fit(exponential_func, xi, yi)
        ax.plot(xi, yi, 'o', label=f'Original Data: {label}')
        ax.plot(xi, exponential_func(xi, *popt), '-', label=f'Fitted Curve: {label}')
    
    ax.legend()
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_title('Exponential Curve Fitting')
    
    return fig