
import numpy as np
import matplotlib.pyplot as plt
import math

def task_func(frequency, sample_size=10000):
    if frequency < 0:
        raise ValueError("Frequency cannot be negative.")
    if sample_size <= 0:
        raise ValueError("Sample size must be positive.")
    
    t = np.linspace(0, 1, sample_size)
    sine_wave = np.sin(2 * math.pi * frequency * t)
    cosine_wave = np.cos(2 * math.pi * frequency * t)
    
    fig, ax = plt.subplots()
    ax.plot(t, sine_wave, label='Sine Wave')
    ax.plot(t, cosine_wave, label='Cosine Wave')
    ax.set_xlabel('Time')
    ax.set_ylabel('Amplitude')
    ax.set_title(f'Sine and Cosine Waves with Frequency {frequency}')
    ax.legend()
    
    return fig, ax