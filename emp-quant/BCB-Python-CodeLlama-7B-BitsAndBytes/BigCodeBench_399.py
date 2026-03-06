
import numpy as np
import matplotlib.pyplot as plt
import math

def task_func(frequency, sample_size=10000):
    if frequency < 0:
        raise ValueError("Frequency must be non-negative")
    if sample_size <= 0:
        raise ValueError("Sample size must be positive")

    # Generate the sine and cosine wave data
    t = np.linspace(0, 1, sample_size)
    x = np.sin(2 * np.pi * frequency * t)
    y = np.cos(2 * np.pi * frequency * t)

    # Create the figure and axes
    fig, ax = plt.subplots()

    # Plot the sine and cosine waves
    ax.plot(t, x, label='Sine wave')
    ax.plot(t, y, label='Cosine wave')

    # Set the x-axis limits
    ax.set_xlim([0, 1])

    # Set the y-axis limits
    ax.set_ylim([-1, 1])

    # Set the title and labels
    ax.set_title('Sine and Cosine Waves')
    ax.set_xlabel('Time')
    ax.set_ylabel('Amplitude')

    # Add a legend
    ax.legend()

    return fig, ax