from random import randint
import matplotlib.pyplot as plt
import numpy as np
def task_func(array_length=100):
    """
    Generate two arrays of random integers and draw a line diagram with the 
    maximum values of the respective elements of the two arrays. Set 'Maximum Values' on its y-axis.

    Parameters:
    - array_length (int): Length of the random arrays to be generated. Default is 100.

    Returns:
    - matplotlib.axes.Axes: Axes object with the plot.

    Requirements:
    - numpy
    - matplotlib.pyplot
    - random

    Example:
    >>> ax = task_func(100)
    """
    array_1 = np.random.randint(0, 100, array_length)
    array_2 = np.random.randint(0, 100, array_length)
    ax = plt.axes()
    ax.plot(array_1, array_2, 'o')
    ax.set_ylabel('Maximum Values')
    ax.set_xlabel('Array 1')
    ax.set_title('Maximum Values')
    return ax