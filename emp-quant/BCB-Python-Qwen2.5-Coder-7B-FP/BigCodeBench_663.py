import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
def task_func(x, y, labels):
    """
    Fits an exponential curve to given data points and plots the curves with labels.
    
    Parameters:
    x (list of np.ndarray): List of x data points for each dataset.
    y (list of np.ndarray): List of y data points for each dataset.
    labels (list of str): List of labels for each dataset.
    
    Returns:
    matplotlib.figure.Figure: The figure object that contains the plotted curves.
    """
    def exponential_func(x, a, b, c):
        return a * np.exp(-b * x) + c
    
    fig, ax = plt.subplots()
    
    for xi, yi, label in zip(x, y, labels):
        popt, _ = curve_fit(exponential_func, xi, yi)
        ax.plot(xi, exponential_func(xi, *popt), label=label)
    
    ax.legend()
    plt.show()
    
    return fig
x = [np.linspace(0, 10, 100), np.linspace(0, 10, 100)]
y = [np.exp(-0.1 * xi) + 0.5 for xi in x]
labels = ['Dataset 1', 'Dataset 2']