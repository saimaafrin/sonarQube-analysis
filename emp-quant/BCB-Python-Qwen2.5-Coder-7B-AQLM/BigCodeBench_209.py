
import numpy as np
from operator import itemgetter
import matplotlib.pyplot as plt

def task_func(data):
    # Convert data to numpy array for easier manipulation
    data = np.array(data)
    
    # Find the tuple with the maximum value at index 1
    max_tuple = max(data, key=itemgetter(1))
    
    # Separate the x and y values
    x_values = data[:, 0]
    y_values = data[:, 1]
    
    # Create the scatter plot
    fig, ax = plt.subplots()
    ax.scatter(x_values, y_values, label='Tuples')
    
    # Highlight the tuple with the maximum value at index 1
    ax.scatter(max_tuple[0], max_tuple[1], color='red', label='Max Tuple')
    
    # Set the title and labels
    ax.set_title('Max Tuple Highlighted')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    
    # Add a legend
    ax.legend()
    
    # Return the Axes object
    return ax