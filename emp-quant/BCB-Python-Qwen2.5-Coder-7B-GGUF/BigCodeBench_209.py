
import numpy as np
from operator import itemgetter
import matplotlib.pyplot as plt

def task_func(data):
    # Convert the input data to a numpy array for easier manipulation
    data_array = np.array(data)
    
    # Find the tuple with the maximum value at index 1
    max_tuple = max(data_array, key=itemgetter(1))
    
    # Separate the x and y values for plotting
    x_values = data_array[:, 0]
    y_values = data_array[:, 1]
    
    # Create the scatter plot
    scatter_plot = plt.scatter(x_values, y_values, label='Tuples')
    
    # Highlight the tuple with the maximum value at index 1
    plt.scatter(max_tuple[0], max_tuple[1], color='red', label='Max Tuple')
    
    # Set the title and labels for the axes
    plt.title('Max Tuple Highlighted')
    plt.xlabel('x')
    plt.ylabel('y')
    
    # Add a legend to the plot
    plt.legend()
    
    # Return the Axes object of the plot
    return scatter_plot.axes