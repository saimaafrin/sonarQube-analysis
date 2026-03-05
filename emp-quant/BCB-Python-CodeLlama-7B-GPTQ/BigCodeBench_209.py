import numpy as np
from operator import itemgetter
import matplotlib.pyplot as plt
def task_func(data):
    """
    Plot a scatter graph of tuples and highlight the tuple with the maximum value at index 1.
    """
    # Create a list of tuples
    data = [(1, 2), (3, 4), (5, 6), (7, 8), (9, 10)]

    # Create a list of x-values
    x = [x for x, y in data]

    # Create a list of y-values
    y = [y for x, y in data]

    # Create a figure and axis object
    fig, ax = plt.subplots()

    # Plot the data as a scatter graph
    ax.scatter(x, y)

    # Find the maximum value at index 1
    max_value = max(data, key=itemgetter(1))

    # Highlight the maximum value at index 1
    ax.scatter(max_value[0], max_value[1], c='red', marker='o')

    # Set the title, x-axis label, and y-axis label
    ax.set_title('Max Tuple Highlighted')
    ax.set_xlabel('x')
    ax.set_ylabel('y')

    # Add a legend
    ax.legend()

    # Return the Axes object
    return ax
data = [(1, 2), (3, 4), (5, 6), (7, 8), (9, 10)]