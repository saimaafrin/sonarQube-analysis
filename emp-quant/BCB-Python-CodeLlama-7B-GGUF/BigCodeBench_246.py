
import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft

ANGLES = np.arange(0, 2*np.pi, 0.01)

def task_func(n_waves, seed=0):
    if n_waves < 1:
        return [], np.array([]), None

    # Generate sine waves with increasing frequency
    sine_waves = []
    for i in range(n_waves):
        freq = 1 / (i + 1)
        sine_waves.append(np.sin(freq * ANGLES + seed))

    # Mix the sine waves
    mixed_signal = np.sum(sine_waves, axis=0)

    # Calculate FFT of mixed signal
    fft_data = fft(mixed_signal)

    # Plot histogram of FFT data
    fig, ax = plt.subplots()
    ax.hist(np.abs(fft_data), bins=50)
    ax.set_xlabel('Frequency')
    ax.set_ylabel('Magnitude')
    ax.set_title('FFT of Mixed Sine Waves')

    return sine_waves, fft_data, ax