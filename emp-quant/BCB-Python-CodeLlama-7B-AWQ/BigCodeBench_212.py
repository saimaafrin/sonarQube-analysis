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

    # Mark the maximum y-value point on the scatter plot
    ax.scatter(*max_y_point, c='red')

    # Set the x and y axis labels
    ax.set_xlabel('x')
    ax.set_ylabel('y')

    # Set the title
    ax.set_title('Points with Max Y Point Highlighted')

    return ax, max_y_point
data = np.random.rand(100, 2)