
import math
from random import randint
import matplotlib.pyplot as plt

def task_func():
    # Generate random parameters for the sine wave
    frequency = randint(1, 10)  # Random frequency between 1 and 10
    amplitude = randint(1, 5)  # Random amplitude between 1 and 5
    phase_shift = randint(0, 360)  # Random phase shift between 0 and 360

    # Generate time points
    time_points = [i * 0.1 for i in range(100)]  # 100 time points from 0 to 10

    # Calculate sine wave values
    sine_wave = [amplitude * math.sin(2 * math.pi * frequency * t + phase_shift) for t in time_points]

    # Create the plot
    fig, ax = plt.subplots()
    ax.plot(time_points, sine_wave)
    ax.set_title('Random Sine Wave')
    ax.set_xlabel('Time')
    ax.set_ylabel('Amplitude')

    # Return the axis object
    return ax