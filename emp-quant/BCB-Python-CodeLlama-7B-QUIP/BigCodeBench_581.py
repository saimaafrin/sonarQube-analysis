
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
    values = [random.randint(-RANGE, RANGE) for i in range(size)]
    # Calculate the sinusoidal values
    sin_values = [math.sin(2 * PI * frequency * i / RANGE) for i in range(size)]
    # Plot the values
    plt.plot(values, sin_values)
    plt.show()

# Call the function
task_func()