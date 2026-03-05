import math
from random import randint
import matplotlib.pyplot as plt
def task_func():
    # Generate random frequency, amplitude, and phase shift
    frequency = randint(1, 10)
    amplitude = randint(1, 10)
    phase_shift = randint(0, 360)

    # Generate time array
    time = np.linspace(0, 10, 1000)

    # Generate sine wave
    sine_wave = amplitude * np.sin(2 * math.pi * frequency * time + phase_shift)

    # Plot sine wave
    fig, ax = plt.subplots()
    ax.plot(time, sine_wave)
    ax.set_title('Random Sine Wave')
    ax.set_xlabel('Time')
    ax.set_ylabel('Amplitude')
    ax.grid()

    return ax