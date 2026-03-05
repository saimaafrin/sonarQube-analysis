import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft
ANGLES = np.arange(0, 2*np.pi, 0.01)
def task_func(n_waves, seed=0):
    """
    Generate a series of n sine waves with increasing frequency with a fidelity of 0.01 radians as provided by the ANGLES array.
    The amplitude of each wave is 1.
    The function returns a list of numpy arrays with the y values of the sine waves.
    Additionally, calculate the Fast Fourier Transform (FFT) of the mixed signal and plot the histogram of the magnitude of the FFT data.
    If n_waves is less than 1, return an empty list for the sine waves, an empty array for the FFT data, and None for the axes object.
    """
    if n_waves < 1:
        return [], np.array([]), None

    # Generate sine waves
    sine_waves = []
    for i in range(n_waves):
        sine_waves.append(np.sin(ANGLES * (i + 1) / n_waves))

    # Mix sine waves
    mixed_signal = np.zeros(len(ANGLES))
    for i in range(n_waves):
        mixed_signal += sine_waves[i]

    # Calculate FFT and plot histogram
    fft_data = fft(mixed_signal)
    hist_data = np.abs(fft_data)
    hist_ax = plt.hist(hist_data, bins=50)

    return sine_waves, fft_data, hist_ax