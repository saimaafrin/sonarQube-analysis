
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
    
    # Create a figure and two subplots
    fig, axs = plt.subplots(2, 1, figsize=(10, 8))
    
    # Plot the original signal
    axs[0].plot(signal, label='Original Signal')
    axs[0].set_title('Original Signal')
    axs[0].legend()
    
    # Plot the transformed signal
    axs[1].stem(np.arange(len(rounded_transformed_signal)), rounded_transformed_signal, use_line_collection=True, label='Transformed Signal')
    axs[1].set_title('Transformed Signal')
    axs[1].legend()
    
    # Adjust layout and display the plot
    plt.tight_layout()
    plt.show()
    
    return rounded_transformed_signal, axs