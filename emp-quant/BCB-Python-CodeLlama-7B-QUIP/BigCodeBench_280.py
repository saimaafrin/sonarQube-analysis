
import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft

def task_func(signal, precision=2, seed=777):
    # Generate a random signal
    np.random.seed(seed)
    signal = np.random.rand(100)

    # Compute the DFT using the FFT algorithm
    dft = fft(signal)

    # Round the transformed signal values to the specified precision
    dft_rounded = np.round(dft, precision)

    # Plot the original signal and the transformed signal
    fig, ax = plt.subplots(nrows=2, ncols=1, sharex=True)
    ax[0].plot(signal)
    ax[1].plot(dft_rounded)
    ax[0].set_title('Original Signal')
    ax[1].set_title('Transformed Signal')
    plt.show()

    return dft_rounded, (ax[0], ax[1])