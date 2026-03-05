import numpy as np
from operator import itemgetter
import matplotlib.pyplot as plt
def task_func(data):
    """
    Plot a scatter graph of tuples and highlight the tuple with the maximum value at index 1.
    """
    # Create a list of tuples
    data = [(1, 2), (3, 4), (5, 6), (7, 8)]

    # Create a figure and axis
    fig, ax = plt.subplots()

    # Plot the data as a scatter graph
    ax.scatter(data, c='blue')

    # Find the maximum value at index 1
    max_value = max(data, key=itemgetter(1))

    # Highlight the maximum value
    ax.scatter(max_value, c='red')

    # Set the title, x-axis label, and y-axis label
    ax.set_title('Max Tuple Highlighted')
    ax.set_xlabel('x')
    ax.set_ylabel('y')

    # Add a legend
    ax.legend()

    return ax
data = [(1, 2), (3, 4), (5, 6), (7, 8)]