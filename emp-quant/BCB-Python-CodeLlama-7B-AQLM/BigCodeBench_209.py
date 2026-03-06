import numpy as np
from operator import itemgetter
import matplotlib.pyplot as plt
def task_func(data):
    """
    Plot a scatter graph of tuples and highlight the tuple with the maximum value at index 1.
    
    Parameters:
    data (list of tuple): A list of tuples where each tuple contains two integers.
    
    Returns:
    matplotlib.axes.Axes: The Axes object of the plot for further manipulation and testing, with the title 'Max Tuple Highlighted', x-axis labeled 'x', y-axis labeled 'y', and a legend.
    
    Requirements:
    - numpy
    - operator
    - matplotlib.pyplot
    
    Example:
    >>> ax = task_func([(10, 20), (30, 40), (25, 50)])
    >>> type(ax)
    <class 'matplotlib.axes._axes.Axes'>
    """
    # Sort the list of tuples by the second value in the tuple
    data.sort(key=itemgetter(1), reverse=True)
    # Get the maximum value at index 1
    max_value = data[0][1]
    # Get the index of the tuple with the maximum value at index 1
    max_index = data.index(data[0])
    # Plot the scatter graph
    ax = plt.scatter([x[0] for x in data], [x[1] for x in data])
    # Highlight the tuple with the maximum value at index 1
    ax.scatter([data[max_index][0]], [data[max_index][1]], marker='*', color='red')
    # Set the title, x-axis label, and y-axis label
    ax.set_title('Max Tuple Highlighted')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    # Add a legend
    ax.legend()
    return ax