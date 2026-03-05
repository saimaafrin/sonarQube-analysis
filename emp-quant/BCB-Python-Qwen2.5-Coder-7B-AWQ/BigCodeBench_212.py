import numpy as np
from operator import itemgetter
import matplotlib.pyplot as plt
def task_func(data):
    """
    Draw a scatter plot of dots and mark the point with the maximum y-value.
    
    Parameters:
    data (list of tuples): A list of (x, y) tuples representing the points.
    
    Returns:
    matplotlib.axes.Axes: Axes object with the scatter plot.
    tuple: The point with the maximum y-value.
    """
    # Convert data to numpy array for easier manipulation
    data_array = np.array(data)
    
    # Find the point with the maximum y-value
    max_y_point = data_array[np.argmax(data_array[:, 1])]
    
    # Create a scatter plot
    fig, ax = plt.subplots()
    ax.scatter(data_array[:, 0], data_array[:, 1], label='Points')
    
    # Highlight the point with the maximum y-value
    ax.scatter(max_y_point[0], max_y_point[1], color='red', label='Max Y Point')
    
    # Set labels and title
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_title('Points with Max Y Point Highlighted')
    ax.legend()
    
    return ax, max_y_point
data = [(1, 2), (3, 5), (4, 4), (2, 3)]