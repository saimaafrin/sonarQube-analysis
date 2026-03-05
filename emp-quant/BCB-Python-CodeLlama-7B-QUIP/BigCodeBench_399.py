
import numpy as np
import matplotlib.pyplot as plt
import math

def task_func(frequency, sample_size=10000):
    if frequency < 0:
        raise ValueError("Frequency must be non-negative")
    if sample_size <= 0:
        raise ValueError("Sample size must be positive")

    # Generate the sine and cosine wave
    t = np.linspace(0, 10, sample_size)
    sine_wave = np.sin(2 * math.pi * frequency * t)
    cosine_wave = np.cos(2 * math.pi * frequency * t)

    # Plot the sine and cosine wave
    fig, ax = plt.subplots()
    ax.plot(t, sine_wave, label='Sine wave')
    ax.plot(t, cosine_wave, label='Cosine wave')
    ax.set_xlabel('Time')
    ax.set_ylabel('Amplitude')
    ax.set_title('Sine and cosine wave')
    ax.legend()
    return fig, ax