
import numpy as np
from operator import itemgetter
import matplotlib.pyplot as plt

def task_func(data):
    # Convert data to numpy array for easier manipulation
    points = np.array(data)
    
    # Find the index of the point with the maximum y-value
    max_y_index = np.argmax(points[:, 1])
    
    # Extract the point with the maximum y-value
    max_y_point = points[max_y_index]
    
    # Create a scatter plot
    fig, ax = plt.subplots()
    ax.scatter(points[:, 0], points[:, 1], label='Data Points')
    
    # Mark the point with the maximum y-value
    ax.scatter(max_y_point[0], max_y_point[1], color='red', label='Max Y Point')
    
    # Set labels and title
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_title('Points with Max Y Point Highlighted')
    ax.legend()
    
    return ax, max_y_point