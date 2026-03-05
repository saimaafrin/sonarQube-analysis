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
    # Generate random signal
    np.random.seed(seed)
    signal = np.random.rand(100)

    # Calculate DFT using FFT
    dft = fft(signal)

    # Round transformed signal values to specified precision
    dft_rounded = np.round(dft, precision)

    # Plot original signal and transformed signal
    fig, (ax1, ax2) = plt.subplots(nrows=2, ncols=1, figsize=(8, 6))
    ax1.plot(signal)
    ax1.set_title('Original Signal')
    ax2.plot(dft_rounded)
    ax2.set_title('Transformed Signal')

    return dft_rounded, (ax1, ax2)
signal = np.random.rand(100)