
import numpy as np
import math
import matplotlib.pyplot as plt
from scipy.signal import get_window

def task_func(amplitude, frequency, time):
    # Generate complex wave with specified amplitude and frequency
    t = np.linspace(0, 1, time)
    x = np.cos(2 * np.pi * frequency * t) + 1j * np.sin(2 * np.pi * frequency * t)

    # Apply Hann window to reduce edge effects
    window = get_window('hann', time)
    x_windowed = x * window

    # Plot complex wave with Hann window
    fig, ax = plt.subplots()
    ax.plot(t, np.real(x_windowed), label='Real part')
    ax.plot(t, np.imag(x_windowed), label='Imaginary part')
    ax.set_xlabel('Time')
    ax.set_ylabel('Amplitude')
    ax.legend()
    ax.set_title('Complex Wave with Hann Window')

    return x_windowed, fig, ax

# Plot the complex wave with Hann window
fig.show()