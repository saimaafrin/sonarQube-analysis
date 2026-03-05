import math
import matplotlib.pyplot as plt
import numpy as np
import random
RANGE = 10000
SIZE = 1000
def task_func(size=SIZE, frequency=1):
    # Generate random x values
    x = np.linspace(0, RANGE, size)
    # Generate random sinusoidal values
    y = np.sin(frequency * x)
    # Create a plot
    fig, ax = plt.subplots()
    ax.plot(x, y)
    return ax