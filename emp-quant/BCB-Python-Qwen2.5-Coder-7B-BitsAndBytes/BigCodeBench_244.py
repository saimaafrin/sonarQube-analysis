
import numpy as np
from scipy.fft import fft
from matplotlib import pyplot as plt

def task_func(original):
    if not original:
        return np.array([]), np.array([]), None
    
    # Create a numeric array from the "original" list
    original_array = np.array(original)
    
    # Calculate Fast Fourier Transform (FFT)
    fft_data = fft(original_array)
    
    # Record the original and FFT data
    print("Original Data:", original_array)
    print("FFT Data:", fft_data)
    
    # Plot the histogram of the magnitude of the FFT data
    fig, ax = plt.subplots()
    magnitudes = np.abs(fft_data)
    ax.hist(magnitudes, bins=30, color='blue', alpha=0.7)
    ax.set_title('Histogram of FFT Magnitude')
    ax.set_xlabel('Magnitude')
    ax.set_ylabel('Frequency')
    
    return original_array, fft_data, ax