
from scipy import fftpack
from matplotlib import pyplot as plt

def task_func(arr):
    # Perform FFT on each row of the array
    fft_coeffs = [fftpack.fft(row) for row in arr]

    # Take the absolute values of the FFT coefficients
    abs_coeffs = [abs(coeff) for coeff in fft_coeffs]

    # Plot the absolute values of the FFT coefficients
    fig, ax = plt.subplots()
    ax.plot(abs_coeffs)
    ax.set_xlabel('Frequency')
    ax.set_ylabel('Amplitude')
    ax.set_title('FFT of 2D Array')
    return ax