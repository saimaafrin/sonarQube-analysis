
import numpy as np
from scipy import fftpack
import matplotlib.pyplot as plt

def task_func(data, sample_rate=8000):
    # Step 1: Add a new key "a" with the value 1 to the dictionary
    data['a'] = 1
    
    # Step 2: Generate a signal based on the values in "data"
    # Assuming the keys in "data" are sorted and represent time points
    time_points = sorted(data.keys())
    signal = [data[time] for time in time_points]
    
    # Step 3: Run a Fast Fourier Transform (FFT) on the signal
    fft_result = fftpack.fft(signal)
    
    # Step 4: Plot and return the FFT of the signal
    freqs = fftpack.fftfreq(len(signal), d=1/sample_rate)
    plt.figure()
    plt.plot(freqs, np.abs(fft_result))
    plt.title('FFT of the signal')
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('Amplitude')
    plt.show()
    
    return fft_result, plt.gca()