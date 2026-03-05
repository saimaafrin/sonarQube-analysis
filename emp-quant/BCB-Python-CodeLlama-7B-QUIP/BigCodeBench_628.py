
import math
from random import randint
import matplotlib.pyplot as plt

def task_func():
    # Generate random frequency, amplitude, and phase shift
    frequency = randint(1, 10)
    amplitude = randint(10, 100)
    phase_shift = randint(0, 360)

    # Calculate the sine wave points
    x = [i * 0.01 for i in range(100)]
    y = [amplitude * math.sin(2 * math.pi * frequency * x[i] + phase_shift) for i in range(100)]

    # Plot the sine wave
    fig, ax = plt.subplots()
    ax.plot(x, y)
    ax.set_title('Random Sine Wave')
    ax.set_xlabel('Time')
    ax.set_ylabel('Amplitude')
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    return ax