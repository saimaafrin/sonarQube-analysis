
import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft

def task_func(signal, precision=2, seed=777):
    # Set the random seed for reproducibility
    np.random.seed(seed)
    
    # Calculate the DFT using FFT
    transformed_signal = fft(signal)
    
    # Round the transformed signal values to the specified precision
    rounded_transformed_signal = np.round(transformed_signal, precision)
    
    # Plot the original signal
    fig, ax1 = plt.subplots()
    ax1.plot(signal, 'b')
    ax1.set_title('Original Signal')
    
    # Plot the transformed signal
    fig, ax2 = plt.subplots()
    ax2.plot(rounded_transformed_signal, 'r')
    ax2.set_title('Transformed Signal')
    
    # Return the rounded transformed signal and the plot axes
    return rounded_transformed_signal, (ax1, ax2)