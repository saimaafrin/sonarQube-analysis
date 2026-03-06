from itertools import chain
import numpy as np
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
def task_func(L):
    '''
    Convert a list of lists 'L' into a single list of integers, standardize the integers, and plot the standardized values.

    Parameters:
    L (list of lists): A list of lists where each sublist contains integers.
    
    Returns:
    matplotlib.axes._axes.Axes: A plot displaying the standardized values.

    Requirements:
    - numpy
    - itertools
    - sklearn.preprocessing
    - matplotlib.pyplot

    Examples:
    >>> ax = task_func([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    '''
    # Convert the list of lists into a single list of integers
    L_flat = list(chain.from_iterable(L))

    # Standardize the integers
    scaler = StandardScaler()
    L_flat_standardized = scaler.fit_transform(L_flat.reshape(-1, 1))

    # Plot the standardized values
    ax = plt.gca()
    ax.plot(L_flat_standardized)
    return ax