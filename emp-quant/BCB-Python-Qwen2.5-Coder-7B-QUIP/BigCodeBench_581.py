
import math
import matplotlib.pyplot as plt
import numpy as np
import random
# Constants
RANGE = 10000
SIZE = 1000
PI = np.pi
def task_func(size=SIZE, frequency=1):
    # Generate random sinusoidal values
    x = np.linspace(0, 2 * PI, size)
    y = np.sin(2 * PI * frequency * x)
    # Add random noise to the values
    y += np.random.normal(0, 0.1, size)
    # Plot the sinusoidal wave
    fig, ax = plt.subplots()
    ax.plot(x, y)
    return ax