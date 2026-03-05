
import numpy as np
from scipy.fft import fft
from matplotlib import pyplot as plt

def task_func(original):
    # Check if the original list is empty
    if not original:
        return np.array([]), None, None
    
    # Create a numeric array from the "original" list
    original_array = np.array(original)
    
    # Calculate the Fast Fourier Transform (FFT)
    fft_data = fft(original_array)
    
    # Calculate the magnitude of the FFT data
    fft_magnitude = np.abs(fft_data)
    
    # Plot the histogram of the magnitude of the FFT data
    fig, ax = plt.subplots()
    ax.hist(fft_magnitude, bins=100, color='k', alpha=0.75)
    ax.set_title('FFT Magnitude Histogram')
    ax.set_xlabel('Magnitude')
    ax.set_ylabel('Frequency')
    
    # Return the numpy array, FFT data, and axes object
    return original_array, fft_data, ax