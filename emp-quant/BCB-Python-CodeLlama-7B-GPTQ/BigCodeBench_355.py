import numpy as np
import math
import matplotlib.pyplot as plt
from scipy.signal import get_window
def task_func(amplitude, frequency, time):
    # Generate complex wave with specified amplitude and frequency
    t = np.linspace(0, 1, time)
    x = np.cos(2 * math.pi * frequency * t) + 1j * np.sin(2 * math.pi * frequency * t)

    # Apply Hann window to reduce edge effects
    window = get_window('hann', time)
    x_windowed = x * window

    # Plot complex wave with Hann window
    fig, ax = plt.subplots()
    ax.plot(t, x_windowed.real, label='Real part')
    ax.plot(t, x_windowed.imag, label='Imaginary part')
    ax.set_title('Complex Wave with Hann Window')
    ax.set_xlabel('Time')
    ax.set_ylabel('Amplitude')
    ax.legend()

    return x, fig, ax