import numpy as np
from operator import itemgetter
import matplotlib.pyplot as plt
def task_func(data):
    """
    Plot a scatter graph of tuples and highlight the tuple with the maximum value at index 1.
    
    Parameters:
    - data: A list of tuples, where each tuple contains two numerical values.
    
    Returns:
    - matplotlib.axes.Axes: The Axes object of the plot.
    """
    # Separate x and y values from the data
    x_values = [item[0] for item in data]
    y_values = [item[1] for item in data]
    
    # Find the tuple with the maximum value at index 1
    max_tuple = max(data, key=itemgetter(1))
    max_x, max_y = max_tuple
    
    # Create the scatter plot
    fig, ax = plt.subplots()
    ax.scatter(x_values, y_values, label='Data Points')
    
    # Highlight the tuple with the maximum value at index 1
    ax.scatter(max_x, max_y, color='red', label='Max Tuple')
    
    # Set the title and labels
    ax.set_title('Max Tuple Highlighted')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    
    # Add a legend
    ax.legend()
    
    return ax