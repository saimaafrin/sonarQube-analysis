import numpy as np
from scipy.optimize import curve_fit
def task_func(x, y, labels):
    """
    Fit an exponential curve to given data points and plot the curves with labels.
    It fits an exponential curve of the form: f(x) = a * exp(-b * x) + c
    to the provided x and y data points for each set of data and plots the fitted curves
    with the corresponding labels on a single matplotlib figure.

    Parameters:
    - x (list of np.ndarray): List of numpy arrays, each representing the x-values of the data points for a dataset.
    - y (list of np.ndarray): List of numpy arrays, each representing the y-values of the data points for a dataset.
    - labels (list of str): List of strings, each representing the label for a dataset.

    Returns:
    - matplotlib.figure.Figure: The figure object that contains the plotted curves.

    Requirements:
    - numpy
    - scipy.optimize

    Example:
    >>> x_data = [np.array([1,2,3]), np.array([4,5,6]), np.array([7,8,9])]
    >>> y_data = [np.array([4,5,6]), np.array([7,8,9]), np.array([10,11,12])]
    >>> labels = ['H2O', 'O2', 'CO2']
    """
    # Create figure
    fig = plt.figure()

    # Fit exponential curve to each dataset
    for i in range(len(x)):
        # Fit exponential curve
        popt, pcov = curve_fit(lambda x, a, b, c: a * np.exp(-b * x) + c, x[i], y[i])
        # Plot fitted curve
        plt.plot(x[i], popt[0] * np.exp(-popt[1] * x[i]) + popt[2], label=labels[i])

    # Set labels and title
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Exponential Curves')

    # Set legend
    plt.legend()

    # Return figure
    return fig