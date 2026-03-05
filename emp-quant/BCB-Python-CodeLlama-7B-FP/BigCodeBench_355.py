import numpy as np
import math
import matplotlib.pyplot as plt
from scipy.signal import get_window
def task_func(amplitude, frequency, time):
    """
    Generates and plots a complex wave with a specified amplitude and frequency over given time points, applying a Hann window to reduce edge effects.
    The wave is represented as a complex number where the real part is the cosine component, and the imaginary part is the sine component.
    It returns both the wave and the plot object.
    """
    # Generate the complex wave
    wave = np.zeros(time.shape, dtype=np.complex128)
    for i in range(time.shape[0]):
        wave[i] = amplitude * np.exp(2j * np.pi * frequency * time[i])

    # Apply the Hann window
    window = get_window('hann', time.shape[0])
    wave *= window

    # Plot the wave
    fig, ax = plt.subplots()
    ax.plot(time, np.real(wave), label='Real Part')
    ax.plot(time, np.imag(wave), label='Imaginary Part')
    ax.set_title('Complex Wave with Hann Window')
    ax.set_xlabel('Time')
    ax.set_ylabel('Amplitude')
    ax.legend()

    return wave, fig, ax
amplitude = 10
frequency = 10
time = np.linspace(0, 10, 1000)