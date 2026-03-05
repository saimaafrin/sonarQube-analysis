
import math
import matplotlib.pyplot as plt
import numpy as np
import random

# Constants
RANGE = 10000
SIZE = 1000
PI = np.pi

def task_func(size=SIZE, frequency=1):
    # Generate a list of random sinusoidal values
    values = [random.uniform(-RANGE, RANGE) for _ in range(size)]
    # Create a sinusoidal function with the given frequency
    def sinusoid(x):
        return math.sin(x * frequency)
    # Plot the sinusoidal function with the random values
    plt.plot(values, sinusoid)
    return plt.gca()

# Call the function and plot the result
task_func()