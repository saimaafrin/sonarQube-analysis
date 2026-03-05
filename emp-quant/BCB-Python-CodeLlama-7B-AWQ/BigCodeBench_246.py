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
        return [], [], None

    # Generate sine waves
    y_list = []
    for i in range(n_waves):
        y_list.append(np.sin(ANGLES * (i + 1) / n_waves))

    # Mix sine waves
    y_mixed = np.sum(y_list, axis=0)

    # Calculate FFT and plot histogram
    fft_data = fft(y_mixed)
    fft_data = np.abs(fft_data)
    plt.hist(fft_data, bins=100, alpha=0.5, label='FFT magnitude')
    plt.legend()
    plt.show()

    return y_list, fft_data, plt.gca()