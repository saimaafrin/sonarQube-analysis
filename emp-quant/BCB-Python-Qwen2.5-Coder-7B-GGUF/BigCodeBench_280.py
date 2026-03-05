
import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft

def task_func(signal, precision=2, seed=777):
    """
    Calculate the one-dimensional discrete N-point Fourier Transform (DFT) for a real or complex sequence (signal) using the Fast Fourier Transform (FFT) algorithm.
    
    Parameters:
    signal (ndarray): The input signal as a numpy array.
    precision (int): The number of decimal places to round the transformed signal values.
    seed (int): The seed for the random number generator to ensure reproducibility.
    
    Returns:
    ndarray: A numpy array of transformed signal values (rounded to the specified precision).
    tuple: A tuple containing the Axes objects for the original signal and transformed signal plots.
    """
    # Set the seed for reproducibility
    np.random.seed(seed)
    
    # Calculate the FFT of the signal
    transformed_signal = fft(signal)
    
    # Round the transformed signal values to the specified precision
    transformed_signal = np.round(transformed_signal, precision)
    
    # Create a figure and axis for the original signal plot
    fig, ax1 = plt.subplots()
    ax1.plot(signal, 'b-')
    ax1.set_title('Original Signal')
    
    # Create a second axis for the transformed signal plot
    ax2 = ax1.twinx()
    ax2.plot(np.abs(transformed_signal), 'r-')
    ax2.set_title('Transformed Signal')
    
    # Return the transformed signal and the Axes objects
    return transformed_signal, (ax1, ax2)