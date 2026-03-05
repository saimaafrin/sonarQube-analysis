import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
def task_func(X, Y):
    """
    Adjust a quadratic function to the given data (X, Y) and plot the data along with the fit.
    The function should output with:
        tuple:
            list: The optimized parameters of the quadratic function (a, b, c).
            matplotlib.axes.Axes: The plot showing the scatter data points and the quadratic fit.
    """
    # Define the quadratic function
    def quadratic(x, a, b, c):
        return a * x ** 2 + b * x + c

    # Define the data
    X = [1, 2, 3, 4, 5]
    Y = [2, 4, 6, 8, 10]

    # Fit the data to the quadratic function
    popt, _ = curve_fit(quadratic, X, Y)

    # Plot the data and the fit
    fig, ax = plt.subplots()
    ax.scatter(X, Y)
    ax.plot(X, quadratic(X, *popt), label='Quadratic fit')
    ax.legend()
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_title('Quadratic Fit')

    # Return the optimized parameters and the plot
    return popt, fig
X = [1, 2, 3, 4, 5]
Y = [2, 4, 6, 8, 10]