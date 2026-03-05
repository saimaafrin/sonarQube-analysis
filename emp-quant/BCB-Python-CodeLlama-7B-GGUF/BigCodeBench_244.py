
import numpy as np
from scipy.fft import fft
from matplotlib import pyplot as plt

def task_func(original):
    # Create a numeric array from the "original" list
    original_array = np.array(original)

    # Calculate Fast Fourier Transform (FFT)
    fft_data = fft(original_array)

    # Record the original and FFT data
    original_data = original_array
    fft_data = fft_data

    # Plot the histogram of the magnitude of the FFT data
    fig, ax = plt.subplots()
    ax.hist(np.abs(fft_data), bins=50)
    ax.set_xlabel('Magnitude')
    ax.set_ylabel('Frequency')
    ax.set_title('FFT Histogram')

    # Return the axes object of the plot
    return original_data, fft_data, ax