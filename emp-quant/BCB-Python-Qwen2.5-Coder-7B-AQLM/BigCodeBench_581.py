
import math
import matplotlib.pyplot as plt
import numpy as np
import random

# Constants
RANGE = 10000
SIZE = 1000
PI = np.pi

def task_func(size=SIZE, frequency=1):
    # Generate random phase shift
    phase_shift = random.uniform(0, 2 * PI)
    
    # Generate x values
    x = np.linspace(0, RANGE, size)
    
    # Generate sinusoidal values
    y = np.sin(frequency * x + phase_shift)
    
    # Plot the sinusoidal wave
    fig, ax = plt.subplots()
    ax.plot(x, y)
    ax.set_title('Sinusoidal Wave')
    ax.set_xlabel('X-axis')
    ax.set_ylabel('Y-axis')
    
    return ax