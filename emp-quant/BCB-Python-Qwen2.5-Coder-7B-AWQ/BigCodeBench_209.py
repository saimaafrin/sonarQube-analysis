import numpy as np
from operator import itemgetter
import matplotlib.pyplot as plt
def task_func(data):
    """
    Plot a scatter graph of tuples and highlight the tuple with the maximum value at index 1.
    
    Parameters:
    data (list of tuples): A list of tuples where each tuple contains two numerical values.
    
    Returns:
    matplotlib.axes.Axes: The Axes object of the plot.
    """
    # Separate x and y values
    x_values = [item[0] for item in data]
    y_values = [item[1] for item in data]
    
    # Find the tuple with the maximum value at index 1
    max_tuple = max(data, key=itemgetter(1))
    max_x, max_y = max_tuple
    
    # Create scatter plot
    ax = plt.scatter(x_values, y_values, label='Data Points')
    
    # Highlight the maximum tuple
    ax.plot(max_x, max_y, 'ro', label='Max Tuple')
    
    # Set plot title and labels
    ax.set_title('Max Tuple Highlighted')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    
    # Add legend
    ax.legend()
    
    return ax