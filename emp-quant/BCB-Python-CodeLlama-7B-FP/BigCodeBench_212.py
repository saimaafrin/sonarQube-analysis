import numpy as np
from operator import itemgetter
import matplotlib.pyplot as plt
def task_func(data):
    """
    Draw a scatter plot of dots and mark the point with the maximum y-value.
    Return the axes object as well as the maximum y-value point.
    """
    # Create a list of random x and y values
    x = np.random.rand(100)
    y = np.random.rand(100)

    # Create a scatter plot
    fig, ax = plt.subplots()
    ax.scatter(x, y)

    # Find the maximum y-value point
    max_y_point = max(zip(x, y), key=itemgetter(1))

    # Mark the maximum y-value point on the plot
    ax.scatter(max_y_point[0], max_y_point[1], c='red', marker='o')

    # Set the x and y axis labels and title
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_title('Points with Max Y Point Highlighted')

    # Return the axes object and the maximum y-value point
    return ax, max_y_point
data = np.random.rand(100, 2)