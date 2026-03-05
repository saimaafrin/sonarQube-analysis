
import numpy as np
from operator import itemgetter
import matplotlib.pyplot as plt

def task_func(data):
    # Extract x and y values from the tuples
    x_values = [item[0] for item in data]
    y_values = [item[1] for item in data]
    
    # Find the tuple with the maximum value at index 1
    max_tuple = max(data, key=itemgetter(1))
    
    # Plot the scatter graph
    fig, ax = plt.subplots()
    ax.scatter(x_values, y_values, c='blue', label='Tuples')
    
    # Highlight the tuple with the maximum value at index 1
    ax.scatter(max_tuple[0], max_tuple[1], c='red', marker='x', label='Max Tuple')
    
    # Set the title and labels
    ax.set_title('Max Tuple Highlighted')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.legend()
    
    return ax