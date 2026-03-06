
import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft

def task_func(signal, precision=2, seed=777):
    # Generate a random real or complex sequence
    np.random.seed(seed)
    signal = np.random.rand(100) + 1j * np.random.rand(100)

    # Perform the DFT using the FFT algorithm
    dft = fft(signal)

    # Round the transformed signal values to the specified precision
    dft_rounded = np.round(dft, precision)

    # Plot the original signal and the transformed signal
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 6))
    ax1.plot(signal)
    ax1.set_title('Original Signal')
    ax2.plot(dft_rounded)
    ax2.set_title('Transformed Signal')
    ax2.set_xlabel('Frequency')
    ax2.set_ylabel('Amplitude')
    plt.show()

    return dft_rounded, (ax1, ax2)

# Call the function with a random real sequence
dft_rounded, (ax1, ax2) = task_func(np.random.rand(100), precision=2, seed=777)

# Call the function with a random complex sequence
dft_rounded, (ax1, ax2) = task_func(np.random.rand(100) + 1j * np.random.rand(100), precision=2, seed=777)