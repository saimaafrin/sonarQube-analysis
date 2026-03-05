from scipy import fftpack
from matplotlib import pyplot as plt
def task_func(arr):
    """
    Perform a Fast Fourier Transform (FFT) on the sum of each row in a 2D array and plot the absolute values of the FFT coefficients.
    
    Parameters:
    arr (numpy.ndarray): A 2D numpy array.
    
    Returns:
    matplotlib.axes.Axes: An Axes object displaying the plot of the absolute values of the FFT coefficients.
    """
    # Sum each row in the 2D array
    row_sums = np.sum(arr, axis=1)
    
    # Perform FFT on the row sums
    fft_result = fftpack.fft(row_sums)
    
    # Calculate the absolute values of the FFT coefficients
    abs_fft_result = np.abs(fft_result)
    
    # Plot the absolute values of the FFT coefficients
    plt.figure()
    plt.plot(abs_fft_result)
    plt.xlabel('Frequency')
    plt.ylabel('Amplitude')
    plt.title('FFT of Row Sums')
    plt.show()
    
    return plt.gca()