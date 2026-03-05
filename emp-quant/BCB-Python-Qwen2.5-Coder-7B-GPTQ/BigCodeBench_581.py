import math
import matplotlib.pyplot as plt
import numpy as np
import random
RANGE = 10000
SIZE = 1000
PI = np.pi
def task_func(size=SIZE, frequency=1):
    # Generate random x values
    x = np.linspace(0, RANGE, size)
    
    # Generate random amplitude values
    amplitudes = [random.uniform(0.5, 2) for _ in range(size)]
    
    # Generate random phase shift values
    phase_shifts = [random.uniform(0, 2*PI) for _ in range(size)]
    
    # Calculate y values as a sum of sinusoidal waves
    y = np.zeros(size)
    for amplitude, phase_shift in zip(amplitudes, phase_shifts):
        y += amplitude * np.sin(frequency * x + phase_shift)
    
    # Create a plot
    fig, ax = plt.subplots()
    ax.plot(x, y)
    ax.set_title('Random Sinusoidal Wave')
    ax.set_xlabel('X-axis')
    ax.set_ylabel('Y-axis')
    
    return ax