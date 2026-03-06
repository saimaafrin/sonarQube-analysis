import matplotlib.pyplot as plt
import numpy as np
from sklearn.preprocessing import StandardScaler
def task_func(x, y, labels):
    """
    Scale the "x" and "y" arrays using the standard scaler of sklearn and plot them with given labels.
    Each pair of x and y arrays are scaled independently and plotted as a separate series with a label.

    Parameters:
    - x (list of np.ndarray): List of numpy arrays representing the x-values of the data points.
    - y (list of np.ndarray): List of numpy arrays representing the y-values of the data points.
    - labels (list of str): List of strings representing the labels for each data series.

    Returns:
    - matplotlib.figure.Figure: The figure object containing the plot.

    Requirements:
    - numpy
    - matplotlib.pyplot
    - sklearn.preprocessing

    Example:
    >>> x = [np.array([1,2,3]), np.array([4,5,6]), np.array([7,8,9])]
    >>> y = [np.array([4,5,6]), np.array([7,8,9]), np.array([10,11,12])]
    >>> labels = ['A', 'B', 'C']
    >>> fig = task_func(x, y, labels)
    >>> plt.show()
    """
    fig = plt.figure()
    for i in range(len(x)):
        x_scaled = StandardScaler().fit_transform(x[i].reshape(-1, 1))
        y_scaled = StandardScaler().fit_transform(y[i].reshape(-1, 1))
        plt.plot(x_scaled, y_scaled, label=labels[i])
    plt.legend()
    return fig