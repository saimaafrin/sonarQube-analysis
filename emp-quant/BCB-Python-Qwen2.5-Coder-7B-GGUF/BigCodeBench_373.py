
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
import numpy as np

def task_func(l, x_data, plot=False):
    """
    Adjust a quadratic curve to the specified data and return the parameters and fitted values.
    
    Parameters:
    l (list): A list of tuples, where each tuple contains x and y values.
    x_data (numpy array): The x-values for which the curve is to be fitted.
    plot (bool, optional): If True, plot the curve and data points. Default is False.
    
    Returns:
    tuple: A tuple containing the following:
        params (numpy array): Parameters of the fitted curve.
        fitted_values (numpy array): Fitted y-values for the provided x_data.
        ax (matplotlib.axes._axes.Axes, optional): Axes object of the plot if plot=True.
    """
    # Extract x and y data from the list of tuples
    x = np.array([point[0] for point in l])
    y = np.array([point[1] for point in l])
    
    # Define the quadratic function
    def quadratic_func(x, a, b, c):
        return a * x**2 + b * x + c
    
    # Perform curve fitting
    params, covariance = curve_fit(quadratic_func, x, y)
    
    # Calculate fitted values
    fitted_values = quadratic_func(x_data, *params)
    
    # Plot the curve and data points if plot is True
    if plot:
        fig, ax = plt.subplots()
        ax.scatter(x, y, color='blue', label='Data points')
        ax.plot(x_data, fitted_values, color='red', label='Fitted curve')
        ax.legend()
        return params, fitted_values, ax
    else:
        return params, fitted_values, None