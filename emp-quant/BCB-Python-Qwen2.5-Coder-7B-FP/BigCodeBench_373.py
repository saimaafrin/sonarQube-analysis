from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
import numpy as np
def task_func(l, x_data, plot=False):
    """
    Adjust a quadratic curve to the specified data and return the parameters and fitted values.
    
    Parameters:
    l (list): A list of tuples, where each tuple contains x and y values for a point.
    x_data (numpy array): The x-values of the data points.
    plot (bool, optional): If True, plot the original data and the fitted curve. Default is False.
    
    Returns:
    tuple: A tuple containing the following:
        params (numpy array): Parameters of the fitted curve.
        fitted_values (numpy array): Fitted y-values for the provided x_data.
        ax (matplotlib.axes._axes.Axes, optional): Axes object of the plot if plot=True.
    """
    # Convert the list of tuples to numpy arrays
    x_data = np.array([point[0] for point in l])
    y_data = np.array([point[1] for point in l])
    
    # Define the quadratic function
    def quadratic_func(x, a, b, c):
        return a * x**2 + b * x + c
    
    # Perform curve fitting
    params, covariance = curve_fit(quadratic_func, x_data, y_data)
    
    # Calculate the fitted values
    fitted_values = quadratic_func(x_data, *params)
    
    # Plotting the original data and the fitted curve if plot=True
    if plot:
        ax = plt.figure().add_subplot(111)
        ax.scatter(x_data, y_data, color='blue', label='Data points')
        ax.plot(x_data, fitted_values, color='red', label='Fitted curve')
        ax.legend()
        return params, fitted_values, ax
    else:
        return params, fitted_values
l = [(1, 2), (2, 3), (3, 5), (4, 8), (5, 12)]
x_data = np.array([point[0] for point in l])