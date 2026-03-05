
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

def task_func(l, x_data, plot=False):
    # Define the quadratic function
    def quadratic(x, a, b, c):
        return a*x**2 + b*x + c

    # Fit the data to the function
    popt, _ = curve_fit(quadratic, x_data, y_data)

    # Extract the parameters
    a, b, c = popt

    # Calculate the fitted values
    fitted_values = quadratic(x_data, a, b, c)

    # Plot the data and the fitted curve
    if plot:
        fig, ax = plt.subplots()
        ax.plot(x_data, y_data, 'bo', label='Data')
        ax.plot(x_data, fitted_values, 'r-', label='Fitted curve')
        ax.legend()
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_title('Quadratic Fit')
        return ax

    # Return the parameters and the fitted values
    return popt, fitted_values

# Fit the data to the quadratic function
params, fitted_values = task_func(x_data, y_data, plot=True)

# Print the parameters and the fitted values
print(params)
print(fitted_values)