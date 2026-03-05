import math
from random import randint
import matplotlib.pyplot as plt
def task_func():
    # Generate random frequency, amplitude, and phase shift
    frequency = randint(1, 10)
    amplitude = randint(1, 10)
    phase_shift = randint(0, 360)

    # Generate sine wave data
    time = [i for i in range(1000)]
    sine_wave = [amplitude * math.sin(2 * math.pi * frequency * t + phase_shift) for t in time]

    # Plot sine wave
    fig, ax = plt.subplots()
    ax.plot(time, sine_wave)
    ax.set_title('Random Sine Wave')
    ax.set_xlabel('Time')
    ax.set_ylabel('Amplitude')
    ax.grid(True)

    return ax