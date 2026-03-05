
from scipy import fftpack
from matplotlib import pyplot as plt

def task_func(arr):
    # Perform FFT on each row of the array
    fft_coeffs = [fftpack.fft(row) for row in arr]
    # Plot the absolute values of the FFT coefficients
    fig, ax = plt.subplots()
    ax.plot(abs(fft_coeffs))
    return ax