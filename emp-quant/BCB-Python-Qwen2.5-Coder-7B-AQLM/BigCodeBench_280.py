
import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft

def task_func(signal, precision=2, seed=777):
    """
    Calculate the one-dimensional discrete N-point Fourier Transform (DFT) for a real or complex sequence (signal) using the Fast Fourier Transform (FFT) algorithm.
    
    Parameters:
    signal (ndarray): The input signal to transform.
    precision (int): The number of decimal places to round the transformed signal values to.
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
    
    # Create a figure and axis for the plots
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 6))
    
    # Plot the original signal
    ax1.plot(signal, label='Original Signal')
    ax1.set_title('Original Signal')
    ax1.legend()
    
    # Plot the transformed signal
    ax2.plot(transformed_signal, label='Transformed Signal')
    ax2.set_title('Transformed Signal')
    ax2.legend()
    
    # Show the plots
    plt.tight_layout()
    plt.show()
    
    # Return the transformed signal and the Axes objects
    return transformed_signal, (ax1, ax2)