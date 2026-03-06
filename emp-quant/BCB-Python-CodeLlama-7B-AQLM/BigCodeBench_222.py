import math
import numpy as np
import matplotlib.pyplot as plt
def task_func(list_input):
    """
    Sort the given list in ascending order based on the degree value of its elements, calculate the cumulative sum of 
    the sorted list, and draw a line chart of the cumulative sum.

    Parameters:
    list_input (list): The list to be sorted.

    Returns:
    tuple: A tuple containing:
           - numpy array: The cumulative sum of the sorted list.
           - matplotlib.axes._axes.Axes: The Axes object of the plotted line chart.

    Requirements:
    - math
    - numpy
    - matplotlib.pyplot

    Example:
    >>> cumsum, ax = task_func([10, 20, 30])
    >>> print(cumsum)
    [10 30 60]
    >>> ax.get_title()
    'Cumulative Sum Plot'
    """
    # Sort the list in ascending order based on the degree value of its elements
    list_input.sort(key=lambda x: x[1])

    # Calculate the cumulative sum of the sorted list
    cumsum = np.cumsum(list(map(lambda x: x[0], list_input)))

    # Draw a line chart of the cumulative sum
    fig, ax = plt.subplots()
    ax.plot(cumsum)
    ax.set_title('Cumulative Sum Plot')
    ax.set_xlabel('Index')
    ax.set_ylabel('Cumulative Sum')
    ax.grid(True)

    return cumsum, ax