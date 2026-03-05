
import math
import matplotlib.pyplot as plt
import numpy as np
import random
# Constants
RANGE = 10000
SIZE = 1000
PI = np.pi
def task_func(size=SIZE, frequency=1):
    # Generate random x values
    x = np.linspace(0, RANGE, size)
    # Generate random sinusoidal values
    y = np.sin(2 * PI * frequency * x) + random.uniform(-0.5, 0.5)
    # Create a plot
    fig, ax = plt.subplots()
    ax.plot(x, y)
    ax.set_title('Random Sinusoidal Wave')
    ax.set_xlabel('X-axis')
    ax.set_ylabel('Y-axis')
    return ax