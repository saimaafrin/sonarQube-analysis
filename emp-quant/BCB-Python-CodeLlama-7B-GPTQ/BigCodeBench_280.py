import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft
def task_func(signal, precision=2, seed=777):
    """
    Calculate the one-dimensional discrete N-point Fourier Transform (DFT) for a real or complex sequence (signal) using the Fast Fourier Transform (FFT) algorithm.
    Plot the original signal and the transformed signal, rounding the transformed signal values to the specified accuracy.
    The title of the plots will be 'Original Signal' and 'Transformed Signal'.
    """
    # Generate a random signal
    np.random.seed(seed)
    signal = np.random.rand(100)

    # Calculate the DFT using the FFT algorithm
    dft = fft(signal)

    # Round the transformed signal values to the specified precision
    dft_rounded = np.round(dft, precision)

    # Plot the original signal and the transformed signal
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))
    ax1.plot(signal, label='Original Signal')
    ax1.set_title('Original Signal')
    ax2.plot(dft_rounded, label='Transformed Signal')
    ax2.set_title('Transformed Signal')
    ax2.set_xlabel('Frequency')
    ax2.set_ylabel('Amplitude')
    ax2.legend()

    return dft_rounded, (ax1, ax2)