import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
def task_func(x, y, labels):
    """
    Fits an exponential curve to given data points and plots the curves with labels.
    
    Parameters:
    x (list of np.ndarray): List of x data points for each set of data.
    y (list of np.ndarray): List of y data points for each set of data.
    labels (list of str): List of labels for each set of data.
    
    Returns:
    matplotlib.figure.Figure: The figure object that contains the plotted curves.
    """
    def exponential_func(x, a, b, c):
        return a * np.exp(-b * x) + c
    
    fig, ax = plt.subplots()
    
    for xi, yi, label in zip(x, y, labels):
        params, _ = curve_fit(exponential_func, xi, yi)
        ax.plot(xi, yi, 'o', label=f'Data {label}')
        ax.plot(xi, exponential_func(xi, *params), '-', label=f'Fit {label}')
    
    ax.legend()
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_title('Exponential Curve Fits')
    
    return fig
x_data = [
    np.array([0, 1, 2, 3, 4, 5]),
    np.array([0, 2, 4, 6, 8, 10])
]
y_data = [
    np.array([1, 0.5, 0.25, 0.125, 0.0625, 0.03125]),
    np.array([0, 2, 4, 6, 8, 10])
]
labels = ['Data 1', 'Data 2']