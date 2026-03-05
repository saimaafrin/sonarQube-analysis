
import math
from random import randint
import matplotlib.pyplot as plt

def task_func():
    # Generate random parameters
    frequency = randint(1, 10)  # Frequency in Hz
    amplitude = randint(1, 5)   # Amplitude
    phase_shift = randint(0, 360)  # Phase shift in degrees

    # Generate time points
    time = [i / 10.0 for i in range(100)]

    # Calculate sine wave
    sine_wave = [amplitude * math.sin(2 * math.pi * frequency * t + math.radians(phase_shift)) for t in time]

    # Create plot
    fig, ax = plt.subplots()
    ax.plot(time, sine_wave)
    ax.set_title('Random Sine Wave')
    ax.set_xlabel('Time')
    ax.set_ylabel('Amplitude')

    return ax