
import numpy as np
from operator import itemgetter
import matplotlib.pyplot as plt

def task_func(data):
    # Convert data to numpy array for easier manipulation
    data = np.array(data)
    
    # Find the point with the maximum y-value
    max_y_point = data[np.argmax(data[:, 1])]
    
    # Create a scatter plot
    fig, ax = plt.subplots()
    ax.scatter(data[:, 0], data[:, 1], label='Points')
    
    # Highlight the point with the maximum y-value
    ax.scatter(max_y_point[0], max_y_point[1], color='red', label='Max Y Point')
    
    # Set labels and title
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_title('Points with Max Y Point Highlighted')
    ax.legend()
    
    return ax, max_y_point