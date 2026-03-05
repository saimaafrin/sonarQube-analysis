import numpy as np
from scipy.fft import fft
from matplotlib import pyplot as plt
def task_func(original):
    # Convert the original list to a numpy array
    original_array = np.array(original)
    
    # Calculate the Fast Fourier Transform (FFT) of the array
    fft_data = fft(original_array)
    
    # Calculate the magnitude of the FFT data
    magnitude_fft = np.abs(fft_data)
    
    # Plot the histogram of the magnitude of the FFT data
    if magnitude_fft.size > 0:
        fig, ax = plt.subplots()
        ax.hist(magnitude_fft, bins=50, color='blue', alpha=0.7)
        ax.set_title('Histogram of FFT Magnitude')
        ax.set_xlabel('Magnitude')
        ax.set_ylabel('Frequency')
    else:
        fig, ax = None, None
    
    # Return the numpy array, FFT data, and axes object
    return original_array, fft_data, ax