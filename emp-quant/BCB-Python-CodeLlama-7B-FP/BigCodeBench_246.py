import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft
ANGLES = np.arange(0, 2*np.pi, 0.01)
def task_func(n_waves, seed=0):
    """
    Generate a series of n sine waves with increasing frequency with a fidelity of 0.01 radians as provided by the ANGLES array.
    The amplitude of each wave is 1.
    The function returns a list of numpy arrays with the y values of the sine waves.
    Additionally, calculate the Fast Fourier Transform (FFT) of the mixed signal and plot the histogram of the magnitude of the FFT data.
    If n_waves is less than 1, return an empty list for the sine waves, an empty array for the FFT data, and None for the axes object.
    """
    if n_waves < 1:
        return [], np.array([]), None

    # Generate sine waves
    sine_waves = []
    for i in range(n_waves):
        sine_waves.append(np.sin(ANGLES * (i + 1)))

    # Mix sine waves
    mixed_signal = np.sum(sine_waves, axis=0)

    # Calculate FFT of mixed signal
    fft_data = fft(mixed_signal)

    # Plot histogram of FFT data
    fig, ax = plt.subplots()
    ax.hist(np.abs(fft_data), bins=50, alpha=0.5, label='FFT magnitude')
    ax.set_xlabel('Frequency')
    ax.set_ylabel('Magnitude')
    ax.set_title('FFT of Mixed Sine Waves')
    ax.legend()

    return sine_waves, fft_data, ax