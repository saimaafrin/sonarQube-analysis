import math
from random import randint
import matplotlib.pyplot as plt
def task_func():
    # Generate random parameters for the sine wave
    frequency = randint(1, 10)  # Random frequency between 1 and 10 Hz
    amplitude = randint(1, 5)   # Random amplitude between 1 and 5
    phase_shift = randint(0, 360)  # Random phase shift between 0 and 360 degrees

    # Generate time points
    time = [i / 100.0 for i in range(0, 1000)]  # Time from 0 to 10 seconds with 1000 points

    # Calculate the sine wave values
    sine_wave = [amplitude * math.sin(2 * math.pi * frequency * t + math.radians(phase_shift)) for t in time]

    # Create the plot
    fig, ax = plt.subplots()
    ax.plot(time, sine_wave)
    ax.set_title('Random Sine Wave')
    ax.set_xlabel('Time')
    ax.set_ylabel('Amplitude')

    return ax