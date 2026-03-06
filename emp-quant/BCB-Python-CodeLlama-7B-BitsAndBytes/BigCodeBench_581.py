
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
    # Create a numpy array from the list
    values_array = np.array(values)
    # Compute the sinusoidal function
    sin_values = np.sin(values_array * frequency * PI / 180)
    # Plot the sinusoidal wave
    plt.plot(values_array, sin_values)
    # Set the title and labels
    plt.title("Sinusoidal Wave")
    plt.xlabel("Values")
    plt.ylabel("Sinusoidal Function")
    # Show the plot
    plt.show()

# Call the function
task_func()