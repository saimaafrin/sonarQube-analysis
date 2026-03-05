
import numpy as np
import matplotlib.pyplot as plt
from random import randint
import math

def task_func(POINTS=100):
    # Initialize the starting point
    x = [0]
    y = [0]

    # Generate random steps
    for _ in range(1, POINTS):
        angle = randint(0, 359)
        x.append(x[-1] + math.cos(angle))
        y.append(y[-1] + math.sin(angle))

    # Convert to numpy arrays
    x = np.array(x)
    y = np.array(y)

    # Plot the path
    fig, ax = plt.subplots()
    ax.plot(x, y, '-o')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_title('Random Walk Path')
    return fig