
import numpy as np
from operator import itemgetter
import matplotlib.pyplot as plt

def task_func(data):
    # Create a list of tuples from the input data
    tuples = [tuple(x) for x in data]

    # Create a NumPy array from the list of tuples
    array = np.array(tuples)

    # Get the maximum value at index 1 from the array
    max_value = array[:, 1].max()

    # Get the index of the maximum value
    max_index = np.where(array[:, 1] == max_value)[0][0]

    # Create a figure and axis object
    fig, ax = plt.subplots()

    # Plot the scatter graph of the tuples
    ax.scatter(array[:, 0], array[:, 1])

    # Highlight the tuple with the maximum value at index 1
    ax.scatter(array[max_index, 0], array[max_index, 1], c='red', marker='o')

    # Set the title, x-axis label, and y-axis label
    ax.set_title('Max Tuple Highlighted')
    ax.set_xlabel('x')
    ax.set_ylabel('y')

    # Add a legend
    ax.legend()

    return ax