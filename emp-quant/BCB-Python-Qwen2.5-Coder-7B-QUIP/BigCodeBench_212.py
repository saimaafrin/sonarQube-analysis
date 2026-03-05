
import numpy as np
from operator import itemgetter
import matplotlib.pyplot as plt

def task_func(data):
    # Convert data to a list of tuples
    points = list(data)
    
    # Find the point with the maximum y-value
    max_y_point = max(points, key=itemgetter(1))
    
    # Create a scatter plot
    fig, ax = plt.subplots()
    ax.scatter(x=points, y=points, c='blue')
    
    # Highlight the point with the maximum y-value
    ax.scatter(max_y_point[0], max_y_point[1], c='red', marker='x')
    
    # Set labels and title
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_title('Points with Max Y Point Highlighted')
    
    # Return the axes object and the maximum y-value point
    return ax, max_y_point