
import numpy as np
from scipy.fft import fft
from matplotlib import pyplot as plt

def task_func(original):
    # Calculate the FFT of the original data
    fft_data = fft(original)

    # Create a numpy array for the original data
    original_array = np.array(original)

    # Plot the histogram of the magnitude of the FFT data
    fig, ax = plt.subplots()
    ax.hist(np.abs(fft_data))

    # Return the axes object of the plot
    return ax