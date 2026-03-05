import numpy as np
import matplotlib.pyplot as plt
import math
def task_func(frequency, sample_size=10000):
    """
    Generate a plot of a sine wave and cosine wave with the given frequency and sample size.

    Parameters:
    frequency (float): The frequency of the sine and cosine waves.
    sample_size (int): The number of samples to generate.

    Returns:
    matplotlib.figure.Figure: The figure object containing the plot.
    matplotlib.axes.Axes: The axes object of the plot.

    Raises:
    ValueError: If the frequency is negative.
    ValueError: If the sample size is non-positive.
    """
    if frequency < 0:
        raise ValueError("Frequency must be non-negative.")
    if sample_size <= 0:
        raise ValueError("Sample size must be positive.")

    t = np.linspace(0, 1, sample_size)
    sine_wave = np.sin(2 * np.pi * frequency * t)
    cosine_wave = np.cos(2 * np.pi * frequency * t)

    fig, ax = plt.subplots()
    ax.plot(t, sine_wave, label='Sine Wave')
    ax.plot(t, cosine_wave, label='Cosine Wave')
    ax.set_xlabel('Time')
    ax.set_ylabel('Amplitude')
    ax.set_title('Sine and Cosine Waves')
    ax.legend()

    return fig, ax