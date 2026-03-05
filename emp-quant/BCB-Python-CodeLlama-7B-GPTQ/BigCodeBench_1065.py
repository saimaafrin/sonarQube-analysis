from scipy import fftpack
from matplotlib import pyplot as plt
def task_func(arr):
    """
    Performs a Fast Fourier Transform (FFT) on the sum of each row in a 2D array and plots the absolute values of the FFT coefficients.
    """
    # Perform FFT on each row of the array
    fft_coeffs = [fftpack.fft(row) for row in arr]

    # Plot the absolute values of the FFT coefficients
    fig, ax = plt.subplots()
    ax.plot(abs(fft_coeffs))
    ax.set_xlabel('Frequency')
    ax.set_ylabel('Amplitude')
    ax.set_title('FFT of Row Sums')
    return ax
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])