import numpy as np
from operator import itemgetter
import matplotlib.pyplot as plt
def task_func(data):
    """
    Draw a scatter plot of dots and mark the point with the maximum y-value. Return the axes object as
    well as the maximum y-value point. 
    
    Parameters:
    data (list of tuples): A list where each tuple contains two floats representing x and y coordinates.
    
    Returns:
    matplotlib.axes.Axes: Axes object with the scatter plot, with the x-axis labeled 'x', the y-axis labeled 'y', and the title 'Points with Max Y Point Highlighted'.
    tuple: The point with the maximum y-value.
    
    Requirements:
    - numpy
    - operator
    - matplotlib.pyplot

    Example:
    >>> ax, point = task_func([(0.1, 0.2), (0.5, 0.6), (0.3, 0.9)])
    >>> type(ax)
    <class 'matplotlib.axes._axes.Axes'>
    """
    # TODO: Implement task_func
    # Hint: Use the following code to get the maximum y-value point
    # max_y_point = max(data, key=itemgetter(1))
    # Hint: Use the following code to draw the scatter plot
    # ax = plt.scatter(data[:, 0], data[:, 1])
    # Hint: Use the following code to mark the point with the maximum y-value
    # ax.scatter(max_y_point[0], max_y_point[1], c='red')
    # Hint: Use the following code to set the x-axis label
    # ax.set_xlabel('x')
    # Hint: Use the following code to set the y-axis label
    # ax.set_ylabel('y')
    # Hint: Use the following code to set the title
    # ax.set_title('Points with Max Y Point Highlighted')
    # Hint: Return the axes object and the maximum y-value point
    return ax, max_y_point