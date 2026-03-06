
from scipy.optimize import curve_fit
import numpy as np
import matplotlib.pyplot as plt

def quadratic_curve(x, a, b, c):
    """Quadratic function."""
    return a * x**2 + b * x + c

def task_func(l, x_data, plot=False):
    """
    Adjust a quadratic curve to the specified data and return the parameters and fitted values.
    
    Parameters:
    l (list or numpy array): The dependent variable data.
    x_data (list or numpy array): The independent variable data.
    plot (bool, optional): Whether to plot the original data and the fitted curve. Default is False.
    
    Returns:
    tuple: A tuple containing the following:
        params (numpy array): Parameters of the fitted curve.
        fitted_values (numpy array): Fitted y-values for the provided x_data.
        ax (matplotlib.axes._axes.Axes, optional): Axes object of the plot if plot=True.
    """
    # Convert input lists to numpy arrays
    l = np.array(l)
    x_data = np.array(x_data)
    
    # Fit the quadratic curve
    params, covariance = curve_fit(quadratic_curve, x_data, l)
    
    # Calculate the fitted values
    fitted_values = quadratic_curve(x_data, *params)
    
    # Plotting
    if plot:
        fig, ax = plt.subplots()
        ax.scatter(x_data, l, label='Original Data')
        ax.plot(x_data, fitted_values, 'r-', label='Fitted Curve', linewidth=2)
        ax.legend()
        plt.show()
        return params, fitted_values, ax
    else:
        return params, fitted_values

    params, fitted_values, ax = task_func(l, x_data, plot=True)
    print("Parameters:", params)
    print("Fitted Values:", fitted_values)