import math
import matplotlib.pyplot as plt
import numpy as np
import random
RANGE = 10000
SIZE = 1000
PI = np.pi
def task_func(size=SIZE, frequency=1):
    """
    Generate a list of random sinusoidal values and plot them in a graph.
    """
    # Generate a list of random sinusoidal values
    values = [random.uniform(-RANGE, RANGE) for _ in range(size)]
    # Calculate the sinusoidal values
    sin_values = [math.sin(2 * PI * frequency * x) for x in values]
    # Plot the sinusoidal values
    fig, ax = plt.subplots()
    ax.plot(values, sin_values)
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_title('Sinusoidal Wave')
    return ax