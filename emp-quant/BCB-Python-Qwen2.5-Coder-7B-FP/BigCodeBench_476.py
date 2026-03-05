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
    
    # Generate x values for the fitted curve
    x_fit = np.linspace(min(X), max(X), 100)
    # Calculate y values for the fitted curve
    y_fit = quadratic_func(x_fit, *params)
    
    # Plot the fitted curve
    ax.plot(x_fit, y_fit, 'r-', label='Quadratic fit')
    
    # Add labels and legend
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.legend()
    
    return params, ax