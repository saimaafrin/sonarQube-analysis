import math
import matplotlib.pyplot as plt
import numpy as np
import random
RANGE = 10000
SIZE = 1000
PI = np.pi
def task_func(size=SIZE, frequency=1):
    """
    Generates a list of random sinusoidal values and plots them in a graph.

    Parameters:
    size (int): The number of points to generate.
    frequency (int): The frequency of the sinusoidal wave.

    Returns:
    Axes object: The plot of the sinusoidal wave.
    """
    # Generate random x values
    x = np.linspace(0, RANGE, size)
    
    # Generate random phase shift
    phase_shift = random.uniform(0, 2 * PI)
    
    # Generate sinusoidal values
    y = np.sin(frequency * x + phase_shift)
    
    # Plot the sinusoidal wave
    fig, ax = plt.subplots()
    ax.plot(x, y)
    ax.set_title('Random Sinusoidal Wave')
    ax.set_xlabel('X-axis')
    ax.set_ylabel('Y-axis')
    
    return ax