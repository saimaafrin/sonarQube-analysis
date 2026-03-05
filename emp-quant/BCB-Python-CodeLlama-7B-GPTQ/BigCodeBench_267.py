import numpy as np
from scipy import fftpack
import matplotlib.pyplot as plt
def task_func(data, sample_rate=8000):
    # Add a new key "a" with the value 1 to the dictionary
    data['a'] = 1

    # Generate a signal based on the values in "data"
    signal = np.zeros(sample_rate)
    for key, value in data.items():
        signal += value * np.sin(2 * np.pi * key * np.arange(sample_rate) / sample_rate)

    # Run a Fast Fourier Transform (FFT) on the signal
    fft = fftpack.fft(signal)

    # Plot and return the FFT of the signal with a title of 'FFT of the signal'
    fig, ax = plt.subplots()
    ax.plot(fft)
    ax.set_title('FFT of the signal')
    return fft, ax
data = {'a': 1, 'b': 2, 'c': 3}
sample_rate = 8000