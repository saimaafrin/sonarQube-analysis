
import numpy as np
from scipy.fft import fft
from matplotlib import pyplot as plt

def task_func(original):
    # Create a numeric array from the "original" list
    original_array = np.array(original)

    # Calculate Fast Fourier Transform (FFT) and record the original and FFT data
    fft_data = fft(original_array)
    original_fft_data = np.abs(fft_data)

    # Plot the histogram of the magnitude of the FFT data
    fig, ax = plt.subplots()
    ax.hist(original_fft_data, bins=100, alpha=0.5, label='FFT data')
    ax.set_xlabel('Magnitude')
    ax.set_ylabel('Count')
    ax.set_title('Histogram of FFT data')
    ax.legend()

    # Return the axes object of the plot
    return original_array, fft_data, ax