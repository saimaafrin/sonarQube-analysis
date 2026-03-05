
import numpy as np
from operator import itemgetter
import matplotlib.pyplot as plt

def task_func(data):
    # Separate the data into x and y coordinates
    x = data[:, 0]
    y = data[:, 1]
    
    # Find the index of the point with the maximum y-value
    max_y_index = np.argmax(y)
    
    # Get the point with the maximum y-value
    max_y_point = (x[max_y_index], y[max_y_index])
    
    # Create a scatter plot
    fig, ax = plt.subplots()
    ax.scatter(x, y, label='Points')
    
    # Highlight the point with the maximum y-value
    ax.scatter(max_y_point[0], max_y_point[1], color='red', label='Max Y Point')
    
    # Set labels and title
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_title('Points with Max Y Point Highlighted')
    ax.legend()
    
    return ax, max_y_point