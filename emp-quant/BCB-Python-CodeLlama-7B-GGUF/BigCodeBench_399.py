
import numpy as np
import matplotlib.pyplot as plt
import math

def task_func(frequency, sample_size=10000):
    if frequency < 0:
        raise ValueError("Frequency must be non-negative")
    if sample_size <= 0:
        raise ValueError("Sample size must be positive")

    t = np.linspace(0, 1, sample_size)
    x = np.sin(2 * math.pi * frequency * t)
    y = np.cos(2 * math.pi * frequency * t)

    fig, ax = plt.subplots()
    ax.plot(t, x, label="Sine wave")
    ax.plot(t, y, label="Cosine wave")
    ax.set_xlabel("Time")
    ax.set_ylabel("Amplitude")
    ax.set_title(f"Sine and Cosine Waves with Frequency {frequency}")
    ax.legend()
    return fig, ax