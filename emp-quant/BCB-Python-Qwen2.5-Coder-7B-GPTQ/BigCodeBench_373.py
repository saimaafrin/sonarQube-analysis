from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
import numpy as np
def quadratic_func(x, a, b, c):
    return a * x**2 + b * x + c
def task_func(l, x_data, plot=False):
    """
    Adjust a quadratic curve to the specified data and return the parameters and fitted values.
    
    Parameters:
    l (list): A list of tuples, where each tuple contains x and y values.
    x_data (numpy array): The x values for which the curve is to be fitted.
    plot (bool, optional): If True, plot the original data and the fitted curve.
    
    Returns:
    tuple: A tuple containing the following:
        params (numpy array): Parameters of the fitted curve.
        fitted_values (numpy array): Fitted y-values for the provided x_data.
        ax (matplotlib.axes._axes.Axes, optional): Axes object of the plot if plot=True.
    """
    # Extract y values from the list of tuples
    y_data = np.array([point[1] for point in l])
    
    # Perform curve fitting
    params, covariance = curve_fit(quadratic_func, x_data, y_data)
    
    # Calculate fitted values
    fitted_values = quadratic_func(x_data, *params)
    
    # Plotting the original data and the fitted curve if plot=True
    if plot:
        ax = plt.figure().add_subplot(111)
        ax.scatter(x_data, y_data, label='Data')
        ax.plot(x_data, fitted_values, 'r-', label='Fitted curve')
        ax.legend()
        return params, fitted_values, ax
    else:
        return params, fitted_values
l = [(1, 2), (2, 4), (3, 6), (4, 8), (5, 10)]
x_data = np.array([1, 2, 3, 4, 5])