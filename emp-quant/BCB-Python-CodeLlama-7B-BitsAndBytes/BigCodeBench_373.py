
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

def task_func(l, x_data, plot=False):
    # Define the quadratic curve
    def quadratic(x, a, b, c):
        return a*x**2 + b*x + c

    # Fit the curve to the data
    params, _ = curve_fit(quadratic, x_data, y_data)

    # Generate the fitted values
    fitted_values = quadratic(x_data, *params)

    # Plot the data and the fitted curve
    if plot:
        fig, ax = plt.subplots()
        ax.plot(x_data, y_data, 'bo', label='Original data')
        ax.plot(x_data, fitted_values, 'r', label='Fitted curve')
        ax.legend()
        plt.show()

    return params, fitted_values, ax

# Fit the curve to the data
params, fitted_values, ax = task_func(x_data, y_data, plot=True)

# Print the parameters and fitted values
print(params)
print(fitted_values)