
import numpy as np
from scipy import fftpack
import matplotlib.pyplot as plt

def task_func(data, sample_rate=8000):
    # Step 1: Add a new key "a" with the value 1 to the dictionary
    data['a'] = 1

    # Step 2: Generate a signal based on the values in "data"
    signal = np.array(list(data.values()))

    # Step 3: Run a Fast Fourier Transform (FFT) on the signal
    fft_result = fftpack.fft(signal)

    # Step 4: Plot and return the FFT of the signal
    plt.figure()
    plt.plot(np.abs(fft_result))
    plt.title('FFT of the signal')
    plt.show()

    return fft_result, plt.gca()