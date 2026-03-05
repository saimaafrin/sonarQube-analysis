import numpy as np
import math
import matplotlib.pyplot as plt
from scipy.signal import get_window
def task_func(amplitude, frequency, time):
    # Generate complex wave with Hann window
    window = get_window('hann', time.size)
    wave = amplitude * np.exp(1j * 2 * np.pi * frequency * time) * window

    # Plot complex wave
    fig, ax = plt.subplots()
    ax.plot(time, wave.real, label='Real')
    ax.plot(time, wave.imag, label='Imaginary')
    ax.set_title('Complex Wave with Hann Window')
    ax.set_xlabel('Time')
    ax.set_ylabel('Amplitude')
    ax.legend()

    return wave, fig, ax