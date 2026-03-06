
import math
import matplotlib.pyplot as plt
import numpy as np
import random

# Constants
RANGE = 10000
SIZE = 1000
PI = np.pi

def task_func(size=SIZE, frequency=1):
    # Generate random x values within the specified range
    x_values = np.linspace(0, RANGE, size)
    
    # Generate random amplitude values
    amplitudes = [random.uniform(0.5, 2) for _ in range(size)]
    
    # Calculate y values using the sinusoidal formula
    y_values = sum(a * np.sin(frequency * PI * x / RANGE) for a in amplitudes)
    
    # Create a figure and an axes.
    fig, ax = plt.subplots()
    
    # Plot the sinusoidal wave
    ax.plot(x_values, y_values)
    
    return ax