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
        phase = np.random.uniform(0, 2*np.pi)
        sine_wave = np.sin(frequency * ANGLES + phase)
        sine_waves.append(sine_wave)

    mixed_signal = np.sum(sine_waves, axis=0)
    fft_data = fft(mixed_signal)

    magnitude = np.abs(fft_data)
    plt.figure()
    plt.hist(magnitude, bins=100, log=True)
    plt.xlabel('Magnitude')
    plt.ylabel('Frequency')
    plt.title('Histogram of FFT Magnitude')
    axes = plt.gca()

    return sine_waves, fft_data, axes