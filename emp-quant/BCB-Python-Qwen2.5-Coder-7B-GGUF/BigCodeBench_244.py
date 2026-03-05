
import numpy as np
from scipy.fft import fft
from matplotlib import pyplot as plt

def task_func(original):
    # Convert the original list to a numpy array
    original_array = np.array(original)
    
    # Calculate the Fast Fourier Transform (FFT) of the original array
    fft_data = fft(original_array)
    
    # Calculate the magnitude of the FFT data
    magnitude_fft = np.abs(fft_data)
    
    # Plot the histogram of the magnitude of the FFT data
    if len(magnitude_fft) > 0:
        fig, ax = plt.subplots()
        ax.hist(magnitude_fft, bins=30, color='blue', alpha=0.7)
        ax.set_title('Histogram of FFT Magnitude')
        ax.set_xlabel('Magnitude')
        ax.set_ylabel('Frequency')
    else:
        fig, ax = plt.subplots()
    
    # Return the original array, FFT data, and the axes object of the plot
    return original_array, fft_data, ax