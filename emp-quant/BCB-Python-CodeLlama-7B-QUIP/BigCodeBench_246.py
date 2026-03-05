
import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft

# Define the angles for the sine waves
ANGLES = np.arange(0, 2*np.pi, 0.01)

def task_func(n_waves, seed=0):
    # Check if n_waves is less than 1, return an empty list for the sine waves and an empty array for the FFT data
    if n_waves < 1:
        return [], [], None

    # Generate the sine waves with increasing frequency
    waves = [np.sin(ANGLES * i * 0.01) for i in range(1, n_waves + 1)]

    # Calculate the Fast Fourier Transform (FFT) of the mixed signal
    fft_data = fft(waves)

    # Plot the histogram of the magnitude of the FFT data
    fig, ax = plt.subplots()
    ax.hist(np.abs(fft_data))

    return waves, fft_data, ax