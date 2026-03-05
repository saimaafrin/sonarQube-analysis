import numpy as np
from scipy.fft import fft
from matplotlib import pyplot as plt
def task_func(original):
    """
    Create a numeric array from the "original" list, calculate Fast Fourier Transform (FFT) and record the original and FFT data. Additionally, plot the histogram of the magnitude of the FFT data and return the axes object of the plot. For an empty list, return an empty array for the FFT data and None for the axes object.
    """
    if not original:
        return np.array([]), np.array([]), None

    original_array = np.array(original)
    fft_data = fft(original_array)

    # Plot the histogram of the magnitude of the FFT data
    fig, ax = plt.subplots()
    ax.hist(np.abs(fft_data), bins=50)
    ax.set_xlabel('Magnitude')
    ax.set_ylabel('Frequency')
    ax.set_title('FFT Histogram')

    return original_array, fft_data, ax
original = [1, 2, 3, 4, 5]