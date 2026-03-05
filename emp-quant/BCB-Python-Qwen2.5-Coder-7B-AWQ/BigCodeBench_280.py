import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft
def task_func(signal, precision=2, seed=777):
    """
    Calculate the one-dimensional discrete N-point Fourier Transform (DFT) for a real or complex sequence (signal) using the Fast Fourier Transform (FFT) algorithm.
    Plot the original signal and the transformed signal, rounding the transformed signal values to the specified accuracy.
    The title of the plots will be 'Original Signal' and 'Transformed Signal'.
    The function should output with:
        ndarray: A numpy array of transformed signal values (rounded to the specified precision).
        tuple: A tuple containing the Axes objects for the original signal and transformed signal plots.
    """
    # Set the random seed for reproducibility
    np.random.seed(seed)
    
    # Calculate the FFT of the signal
    transformed_signal = fft(signal)
    
    # Round the transformed signal values to the specified precision
    rounded_transformed_signal = np.round(transformed_signal, precision)
    
    # Create a figure and axis for the original signal plot
    fig, ax1 = plt.subplots()
    ax1.plot(signal, 'b-')
    ax1.set_xlabel('Time')
    ax1.set_ylabel('Amplitude', color='b')
    ax1.set_title('Original Signal')
    
    # Create a second y-axis for the transformed signal plot
    ax2 = ax1.twinx()
    ax2.plot(rounded_transformed_signal, 'r-')
    ax2.set_ylabel('Amplitude', color='r')
    
    # Show the plots
    plt.show()
    
    # Return the rounded transformed signal and the Axes objects
    return rounded_transformed_signal, (ax1, ax2)