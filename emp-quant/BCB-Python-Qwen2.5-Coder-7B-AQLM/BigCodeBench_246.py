
import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft

ANGLES = np.arange(0, 2*np.pi, 0.01)

def task_func(n_waves, seed=0):
    if n_waves < 1:
        return [], np.array([]), None

    np.random.seed(seed)
    sine_waves = []
    frequencies = np.linspace(1, n_waves, n_waves)
    t = np.arange(0, len(ANGLES))

    for freq in frequencies:
        y = np.sin(freq * t + np.random.uniform(0, 2*np.pi))
        sine_waves.append(y)

    mixed_signal = np.sum(sine_waves, axis=0)
    fft_data = fft(mixed_signal)
    magnitude = np.abs(fft_data)

    fig, ax = plt.subplots()
    ax.hist(magnitude, bins=50, log=True)
    ax.set_title('FFT Magnitude Histogram')
    ax.set_xlabel('Magnitude')
    ax.set_ylabel('Frequency')

    return sine_waves, fft_data, ax