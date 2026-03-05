
import numpy as np
import math
import matplotlib.pyplot as plt
from scipy.signal import get_window

def task_func(amplitude, frequency, time):
    """
    Generates and plots a complex wave with a specified amplitude and frequency over given time points,
    applying a Hann window to reduce edge effects. The wave is represented as a complex number where the real part
    is the cosine component, and the imaginary part is the sine component. It returns both the wave and the plot object.

    Parameters:
    amplitude (float): The amplitude of the wave.
    frequency (float): The frequency of the wave.
    time (numpy.ndarray): The time points over which to generate the wave.

    Returns:
    numpy.ndarray: The generated complex wave as a numpy array of complex numbers.
    matplotlib.figure.Figure: The figure object of the plot.
    matplotlib.axes.Axes: The axes object of the plot.
    """
    # Generate the Hann window
    window = get_window('hann', len(time))
    
    # Generate the complex wave
    real_part = amplitude * np.cos(2 * math.pi * frequency * time)
    imag_part = amplitude * np.sin(2 * math.pi * frequency * time)
    complex_wave = real_part + 1j * imag_part
    
    # Apply the Hann window
    complex_wave_windowed = complex_wave * window
    
    # Plot the complex wave
    fig, ax = plt.subplots()
    ax.plot(time, np.real(complex_wave_windowed), label='Real Part')
    ax.plot(time, np.imag(complex_wave_windowed), label='Imaginary Part')
    ax.set_title('Complex Wave with Hann Window')
    ax.set_xlabel('Time')
    ax.set_ylabel('Amplitude')
    ax.legend()
    
    return complex_wave_windowed, fig, ax