
from scipy import fftpack
from matplotlib import pyplot as plt

def task_func(arr):
    """
    Performs a Fast Fourier Transform (FFT) on the sum of each row in a 2D array and plots the absolute values of the FFT coefficients.
    
    Parameters:
    arr (numpy.ndarray): A 2D numpy array.
    
    Returns:
    matplotlib.axes.Axes: An Axes object displaying the plot of the absolute values of the FFT coefficients.
    """
    # Sum of each row
    row_sums = np.sum(arr, axis=1)
    
    # Perform FFT on the row sums
    fft_result = fftpack.fft(row_sums)
    
    # Compute the absolute values of the FFT coefficients
    abs_fft_result = np.abs(fft_result)
    
    # Plot the absolute values of the FFT coefficients
    fig, ax = plt.subplots()
    ax.plot(abs_fft_result)
    ax.set_title('Absolute Values of FFT Coefficients')
    ax.set_xlabel('Index')
    ax.set_ylabel('Absolute Value')
    
    return ax