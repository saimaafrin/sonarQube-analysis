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
    # Calculate the sinusoidal function
    sin_values = [math.sin(frequency * value) for value in values]
    # Plot the sinusoidal function
    fig, ax = plt.subplots()
    ax.plot(values, sin_values)
    ax.set_xlabel('Value')
    ax.set_ylabel('Sinusoidal Value')
    ax.set_title('Sinusoidal Function')
    return fig