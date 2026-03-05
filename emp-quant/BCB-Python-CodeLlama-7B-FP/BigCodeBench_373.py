from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
def task_func(l, x_data, plot=False):
    """
    Adjust a quadratic curve to the specified data and return the parameters and fitted values.
    """
    # Define the quadratic function
    def quadratic(x, a, b, c):
        return a * x ** 2 + b * x + c

    # Fit the data to the quadratic function
    popt, _ = curve_fit(quadratic, x_data, y_data)

    # Generate the fitted values
    fitted_values = quadratic(x_data, *popt)

    # Plot the data and the fitted curve
    if plot:
        fig, ax = plt.subplots()
        ax.plot(x_data, y_data, 'bo', label='Data')
        ax.plot(x_data, fitted_values, 'r', label='Fitted curve')
        ax.legend()
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_title('Quadratic Fit')
        return ax

    # Return the parameters and fitted values
    return popt, fitted_values
x_data = [1, 2, 3, 4, 5]
y_data = [1, 4, 9, 16, 25]