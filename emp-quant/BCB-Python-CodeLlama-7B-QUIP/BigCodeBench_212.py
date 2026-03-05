
import numpy as np
from operator import itemgetter
import matplotlib.pyplot as plt

def task_func(data):
    # Calculate the maximum y-value
    max_y = max(data, key=itemgetter(1))[1]

    # Create a figure and axes objects
    fig, ax = plt.subplots()

    # Plot the data as a scatter plot
    ax.scatter(data[:, 0], data[:, 1])

    # Add a label to the y-axis
    ax.set_ylabel('y')

    # Add a label to the x-axis
    ax.set_xlabel('x')

    # Add a title to the plot
    ax.set_title('Points with Max Y Point Highlighted')

    # Add a marker to the maximum y-value point
    ax.scatter([data[max_y][0]], [data[max_y][1]], marker='x')

    # Return the axes object and the maximum y-value point
    return ax, data[max_y]