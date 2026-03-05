
import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft

def task_func(signal, precision=2, seed=777):
    # Generate a random real or complex sequence
    np.random.seed(seed)
    signal = np.random.rand(100) + 1j * np.random.rand(100)

    # Calculate the one-dimensional discrete N-point Fourier Transform (DFT)
    # using the Fast Fourier Transform (FFT) algorithm
    transformed_signal = fft(signal)

    # Round the transformed signal values to the specified precision
    transformed_signal = np.round(transformed_signal, precision)

    # Plot the original signal and the transformed signal
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))
    ax1.plot(signal)
    ax1.set_title('Original Signal')
    ax2.plot(transformed_signal)
    ax2.set_title('Transformed Signal')
    plt.show()

    return transformed_signal, (ax1, ax2)