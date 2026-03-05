import numpy as np
from scipy import fftpack
import matplotlib.pyplot as plt
def task_func(data, sample_rate=8000):
    # Add a new key "a" with the value 1 to the dictionary
    data['a'] = 1
    
    # Generate a signal based on the values in "data"
    time = np.arange(len(data)) / sample_rate
    signal = np.sum([data[key] * np.sin(2 * np.pi * key * time) for key in data], axis=0)
    
    # Run a Fast Fourier Transform (FFT) on the signal
    fft_result = fftpack.fft(signal)
    
    # Plot and return the FFT of the signal with a title of 'FFT of the signal'
    plt.figure()
    plt.plot(np.abs(fft_result))
    plt.title('FFT of the signal')
    plt.xlabel('Frequency')
    plt.ylabel('Amplitude')
    plt.show()
    
    return fft_result, plt.gca()