
import numpy as np
from operator import itemgetter
import matplotlib.pyplot as plt

def task_func(data):
    # Create a list of tuples with the x and y values
    points = [(x, y) for x, y in zip(data['x'], data['y'])]

    # Find the maximum y-value and its corresponding x-value
    max_y_value = max(points, key=itemgetter(1))[1]
    max_y_x_value = max(points, key=itemgetter(1))[0]

    # Create a scatter plot with the points
    fig, ax = plt.subplots()
    ax.scatter(data['x'], data['y'])

    # Add a vertical line to mark the maximum y-value
    ax.axvline(x=max_y_x_value, color='red')

    # Add a label to the vertical line
    ax.text(max_y_x_value, max_y_value, f'Max Y Value: {max_y_value}', ha='center', va='bottom')

    # Set the title and labels
    ax.set_title('Points with Max Y Point Highlighted')
    ax.set_xlabel('x')
    ax.set_ylabel('y')

    # Return the axes object and the maximum y-value point
    return ax, (max_y_x_value, max_y_value)