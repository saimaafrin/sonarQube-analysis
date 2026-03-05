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
        y_values = np.sin(frequency * ANGLES)
        sine_waves.append(y_values)

    mixed_signal = np.sum(sine_waves, axis=0)
    fft_data = fft(mixed_signal)
    magnitude_fft = np.abs(fft_data)

    plt.figure()
    plt.hist(magnitude_fft, bins=100)
    plt.xlabel('Magnitude')
    plt.ylabel('Frequency')
    plt.title('Histogram of FFT Magnitude')
    plt.show()

    return sine_waves, fft_data, plt.gca()