import numpy as np
from scipy.fft import fft
from matplotlib import pyplot as plt
def task_func(original):
    """
    Create a numeric array from the "original" list, calculate Fast Fourier Transform (FFT) and record the original and FFT data.
    Additionally, plot the histogram of the magnitude of the FFT data and return the original and FFT data along with the axes object of the plot.
    For an empty list, return an empty array for the FFT data and None for the axes object.
    
    :param original: List of numeric values.
    :return: Tuple containing:
             - np.array: A numpy array for the original data.
             - np.array: FFT data.
             - plt.Axes: The axes object of the plot.
    """
    # Convert the original list to a numpy array
    original_array = np.array(original)
    
    # Calculate the FFT of the original array
    fft_data = fft(original_array)
    
    # Check if the original list is empty
    if len(original) == 0:
        return original_array, fft_data, None
    
    # Calculate the magnitude of the FFT data
    magnitude_fft = np.abs(fft_data)
    
    # Plot the histogram of the magnitude of the FFT data
    fig, ax = plt.subplots()
    ax.hist(magnitude_fft, bins=30, color='blue', alpha=0.7)
    ax.set_title('Histogram of FFT Magnitude')
    ax.set_xlabel('Magnitude')
    ax.set_ylabel('Frequency')
    
    return original_array, fft_data, ax