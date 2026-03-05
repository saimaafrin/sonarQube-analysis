
import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft

ANGLES = np.arange(0, 2*np.pi, 0.01)

def task_func(n_waves, seed=0):
    if n_waves < 1:
        return [], np.array([]), None
    
    np.random.seed(seed)
    sine_waves = []
    for i in range(n_waves):
        frequency = i + 1
        time = np.arange(0, 2*np.pi, 0.01)
        wave = np.sin(frequency * time + np.random.uniform(0, 2*np.pi))
        sine_waves.append(wave)
    
    mixed_signal = np.sum(sine_waves, axis=0)
    fft_data = fft(mixed_signal)
    magnitude = np.abs(fft_data)
    
    fig, ax = plt.subplots()
    ax.hist(magnitude, bins=100, color='blue', alpha=0.7)
    ax.set_title('Histogram of FFT Magnitude')
    ax.set_xlabel('Magnitude')
    ax.set_ylabel('Frequency')
    
    return sine_waves, fft_data, ax