
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

def task_func(X, Y):
    # Define the quadratic function
    def quadratic_func(x, a, b, c):
        return a * x**2 + b * x + c

    # Perform curve fitting
    params, covariance = curve_fit(quadratic_func, X, Y)

    # Extract the optimized parameters
    a, b, c = params

    # Create the plot
    fig, ax = plt.subplots()
    ax.scatter(X, Y, label='Data points')
    ax.plot(X, quadratic_func(X, a, b, c), 'r-', label='Quadratic fit')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.legend()
    plt.show()

    # Return the optimized parameters and the plot
    return params, ax