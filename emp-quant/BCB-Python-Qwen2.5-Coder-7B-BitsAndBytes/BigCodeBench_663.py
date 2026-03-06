
import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

def task_func(x, y, labels):
    """
    Fits an exponential curve to given data points and plots the curves with labels.

    Parameters:
    x (list or array): The x-coordinates of the data points.
    y (list or array): The y-coordinates of the data points.
    labels (list): A list of labels for each set of data points.

    Returns:
    matplotlib.figure.Figure: The figure object that contains the plotted curves.
    """

    # Define the exponential function
    def exponential_func(x, a, b, c):
        return a * np.exp(-b * x) + c

    fig, ax = plt.subplots()

    for i in range(len(x)):
        # Fit the exponential curve to the data
        popt, pcov = curve_fit(exponential_func, x[i], y[i])
        
        # Generate the fitted curve
        x_fit = np.linspace(min(x[i]), max(x[i]), 100)
        y_fit = exponential_func(x_fit, *popt)
        
        # Plot the original data points
        ax.scatter(x[i], y[i], label=f'Data {i+1}')
        
        # Plot the fitted curve
        ax.plot(x_fit, y_fit, label=f'Fitted Curve {i+1}')

    # Add legend and labels
    ax.legend()
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_title('Exponential Curve Fitting')

    return fig

    fig = task_func(x_data, y_data, labels)
    plt.show()