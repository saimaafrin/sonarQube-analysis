
import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft

ANGLES = np.arange(0, 2*np.pi, 0.01)

def task_func(n_waves, seed=0):
    if n_waves < 1:
        return [], [], None
    
    np.random.seed(seed)
    sine_waves = []
    for i in range(n_waves):
        frequency = i + 1
        sine_wave = np.sin(frequency * ANGLES)
        sine_waves.append(sine_wave)
    
    mixed_signal = np.sum(sine_waves, axis=0)
    fft_data = fft(mixed_signal)
    
    plt.figure()
    plt.hist(np.abs(fft_data), bins=50)
    plt.xlabel('Frequency')
    plt.ylabel('Magnitude')
    axes = plt.gca()
    
    return sine_waves, fft_data, axes