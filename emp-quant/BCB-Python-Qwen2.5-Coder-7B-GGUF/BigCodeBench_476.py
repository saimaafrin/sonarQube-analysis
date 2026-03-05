
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

def quadratic_func(x, a, b, c):
    return a * x**2 + b * x + c

def task_func(X, Y):
    # Fit the quadratic function to the data
    params, covariance = curve_fit(quadratic_func, X, Y)
    
    # Create a plot
    fig, ax = plt.subplots()
    ax.scatter(X, Y, label='Data points')
    ax.plot(X, quadratic_func(X, *params), 'r-', label='Quadratic fit')
    ax.legend()
    
    return params, ax