import numpy as np
import matplotlib.pyplot as plt
import math
def task_func(frequency, sample_size=10000):
    """
    Create a diagram of a sine wave and cosine wave with a given frequency and return the plot.

    Args:
        frequency (float): The frequency of the sine and cosine waves.
        sample_size (int, optional): The number of samples to use for the plot. Defaults to 10000.

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

    # Generate the sine and cosine wave data
    t = np.linspace(0, 1, sample_size)
    x = np.sin(2 * np.pi * frequency * t)
    y = np.cos(2 * np.pi * frequency * t)

    # Create the plot
    fig, ax = plt.subplots()
    ax.plot(t, x, label="Sine wave")
    ax.plot(t, y, label="Cosine wave")
    ax.set_xlabel("Time")
    ax.set_ylabel("Amplitude")
    ax.set_title(f"Sine and Cosine Waves with Frequency {frequency}")
    ax.legend()

    return fig, ax