
import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft

ANGLES = np.arange(0, 2 * np.pi, 0.01)

def task_func(n_waves, seed=0):
    if n_waves < 1:
        return [], np.array([]), None
    
    np.random.seed(seed)
    sine_waves = []
    frequencies = np.linspace(1, n_waves, n_waves)
    
    for freq in frequencies:
        t = np.arange(0, len(ANGLES))
        y = np.sin(freq * ANGLES + np.random.normal(0, 0.1, len(ANGLES)))
        sine_waves.append(y)
    
    mixed_signal = np.sum(sine_waves, axis=0)
    fft_data = fft(mixed_signal)
    
    fig, ax = plt.subplots()
    ax.hist(np.abs(fft_data), bins=50, color='blue', alpha=0.7)
    ax.set_title('Histogram of FFT Magnitude')
    ax.set_xlabel('Magnitude')
    ax.set_ylabel('Frequency')
    
    return sine_waves, fft_data, ax