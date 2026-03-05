
from scipy import fftpack
from matplotlib import pyplot as plt

def task_func(arr):
    # Perform FFT on each row of the 2D array
    fft_coeffs = [fftpack.fft(row) for row in arr]
    
    # Plot the absolute values of the FFT coefficients
    fig, ax = plt.subplots()
    ax.plot(abs(fft_coeffs))
    ax.set_xlabel('Frequency')
    ax.set_ylabel('Amplitude')
    ax.set_title('FFT of 2D Array')
    return ax