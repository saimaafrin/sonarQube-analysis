
import numpy as np
from operator import itemgetter
import matplotlib.pyplot as plt

def task_func(data):
    # Create a list of tuples
    tuples = [(i, i**2) for i in range(1, 10)]

    # Find the tuple with the maximum value at index 1
    max_tuple = max(tuples, key=itemgetter(1))

    # Plot the scatter graph
    fig, ax = plt.subplots()
    ax.scatter(x=list(range(1, 10)), y=list(map(itemgetter(1), tuples)), label='y')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_title('Max Tuple Highlighted')
    ax.legend()
    return ax