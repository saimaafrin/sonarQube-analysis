import math
import matplotlib.pyplot as plt
import numpy as np
import random
RANGE = 10000
SIZE = 1000
def task_func(size=SIZE, frequency=1):
    """
    Generate a list of random sinusoidal values and plot them in a graph.
    """
    # Generate a list of random sinusoidal values
    values = [random.uniform(-RANGE, RANGE) for _ in range(size)]
    # Create a new figure and axis object
    fig, ax = plt.subplots()
    # Plot the sinusoidal wave
    ax.plot(values, label='Sinusoidal wave')
    # Set the x-axis label and title
    ax.set_xlabel('X-axis')
    ax.set_ylabel('Y-axis')
    ax.set_title('Sinusoidal Wave')
    # Return the Axes object
    return ax