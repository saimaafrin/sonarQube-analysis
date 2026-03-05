
import numpy as np
import math
import matplotlib.pyplot as plt
from scipy.signal import get_window

def task_func(amplitude, frequency, time):
    # Generate time points
    t = np.linspace(0, 2 * math.pi, time, endpoint=False)
    
    # Generate the complex wave
    wave = amplitude * np.exp(1j * frequency * t)
    
    # Apply Hann window
    window = get_window('hann', len(t))
    wave = wave * window
    
    # Plot the wave
    fig, ax = plt.subplots()
    ax.plot(t, wave.real, label='Real part')
    ax.plot(t, wave.imag, label='Imaginary part')
    ax.set_title('Complex Wave with Hann Window')
    ax.set_xlabel('Time')
    ax.set_ylabel('Amplitude')
    ax.legend()
    
    return wave, fig, ax