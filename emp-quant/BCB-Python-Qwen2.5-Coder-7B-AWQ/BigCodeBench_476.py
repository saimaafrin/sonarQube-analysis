import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
def task_func(X, Y):
    """
    Adjusts a quadratic function to the given data (X, Y) and plots the data along with the fit.
    
    Parameters:
    X (list or array): The x-coordinates of the data points.
    Y (list or array): The y-coordinates of the data points.
    
    Returns:
    tuple:
        list: The optimized parameters of the quadratic function (a, b, c).
        matplotlib.axes.Axes: The plot showing the scatter data points and the quadratic fit.
    """
    # Define the quadratic function
    def quadratic_func(x, a, b, c):
        return a * x**2 + b * x + c
    
    # Perform curve fitting
    params, covariance = curve_fit(quadratic_func, X, Y)
    
    # Create a plot
    fig, ax = plt.subplots()
    ax.scatter(X, Y, label='Data points')
    ax.plot(X, quadratic_func(X, *params), 'r-', label='Quadratic fit')
    ax.legend()
    
    return params, ax