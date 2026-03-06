
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

def quadratic_function(x, a, b, c):
    return a * x**2 + b * x + c

def task_func(X, Y):
    # Fit the quadratic function to the data
    popt, pcov = curve_fit(quadratic_function, X, Y)
    
    # Extract the optimized parameters
    a, b, c = popt
    
    # Create a figure and axis for plotting
    fig, ax = plt.subplots()
    
    # Plot the original data points
    ax.scatter(X, Y, color='blue', label='Data Points')
    
    # Generate x values for the fitted curve
    x_fit = np.linspace(min(X), max(X), 300)
    
    # Calculate y values for the fitted curve
    y_fit = quadratic_function(x_fit, a, b, c)
    
    # Plot the fitted curve
    ax.plot(x_fit, y_fit, color='red', label='Quadratic Fit')
    
    # Add labels and legend
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.legend()
    
    # Show the plot
    plt.show()
    
    # Return the optimized parameters and the plot
    return (a, b, c), ax