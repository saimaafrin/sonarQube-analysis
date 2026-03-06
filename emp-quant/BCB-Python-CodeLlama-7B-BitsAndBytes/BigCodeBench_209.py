
import numpy as np
from operator import itemgetter
import matplotlib.pyplot as plt

def task_func(data):
    # Create a list of tuples from the input data
    tuples = [tuple(x) for x in data]

    # Find the maximum value at index 1 in the list of tuples
    max_value = max(tuples, key=itemgetter(1))

    # Create a figure and axis object
    fig, ax = plt.subplots()

    # Plot the scatter graph of the tuples
    ax.scatter(x=[x[0] for x in tuples], y=[x[1] for x in tuples])

    # Highlight the tuple with the maximum value at index 1
    ax.scatter(x=[max_value[0]], y=[max_value[1]], c='red', marker='o')

    # Set the title, x-axis label, and y-axis label
    ax.set_title('Max Tuple Highlighted')
    ax.set_xlabel('x')
    ax.set_ylabel('y')

    # Add a legend
    ax.legend()

    return ax

# Show the plot
plt.show()