import numpy as np
from operator import itemgetter
import matplotlib.pyplot as plt
def task_func(data):
    # Create a scatter plot of the data
    fig, ax = plt.subplots()
    ax.scatter(data[:, 0], data[:, 1], c='blue')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_title('Points with Max Y Point Highlighted')

    # Find the point with the maximum y-value
    max_y_point = max(data, key=itemgetter(1))

    # Mark the point with the maximum y-value
    ax.scatter(max_y_point[0], max_y_point[1], c='red')

    # Return the axes object and the maximum y-value point
    return ax, max_y_point
data = np.array([[1, 2], [2, 3], [3, 4], [4, 5], [5, 6]])