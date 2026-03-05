import numpy as np
import matplotlib.pyplot as plt
import math
def task_func(frequency, sample_size=10000):
    # Check if the frequency is negative
    if frequency < 0:
        raise ValueError("Frequency cannot be negative.")
    
    # Check if the sample size is non-positive
    if sample_size <= 0:
        raise ValueError("Sample size must be positive.")
    
    # Generate time points
    t = np.linspace(0, 1, sample_size)
    
    # Calculate sine and cosine values
    sine_wave = np.sin(2 * np.pi * frequency * t)
    cosine_wave = np.cos(2 * np.pi * frequency * t)
    
    # Create a figure and axis
    fig, ax = plt.subplots()
    
    # Plot the sine and cosine waves
    ax.plot(t, sine_wave, label='Sine Wave')
    ax.plot(t, cosine_wave, label='Cosine Wave')
    
    # Set labels and title
    ax.set_xlabel('Time')
    ax.set_ylabel('Amplitude')
    ax.set_title('Sine and Cosine Waves')
    ax.legend()
    
    # Return the figure and axis objects
    return fig, ax