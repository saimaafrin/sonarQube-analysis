
import numpy as np
from scipy import fftpack
import matplotlib.pyplot as plt

def task_func(data, sample_rate=8000):
    # Add a new key "a" with the value 1 to the dictionary
    data['a'] = 1
    
    # Generate a signal based on the values in "data"
    time = np.arange(len(data)) / sample_rate
    signal = np.array(list(data.values()))
    
    # Run a Fast Fourier Transform (FFT) on the signal
    fft_result = fftpack.fft(signal)
    
    # Calculate the frequency axis
    freqs = fftpack.fftfreq(len(fft_result), d=1/sample_rate)
    
    # Plot and return the FFT of the signal
    fig, ax = plt.subplots()
    ax.plot(freqs[:len(freqs)//2], np.abs(fft_result)[:len(fft_result)//2])
    ax.set_title('FFT of the signal')
    plt.show()
    
    return fft_result, ax