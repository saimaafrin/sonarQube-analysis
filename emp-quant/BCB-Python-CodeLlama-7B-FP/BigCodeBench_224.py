import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft
def task_func(range_start=-10, range_end=10, step=0.1):
    """
    Generates a sequence of tuples containing x, sin(x), cos(x), and abs(sin(x) - cos(x)) values.
    Plots the sine and cosine functions using these values along with the absolute difference between the two functions.
    Returns the plot and the magnitude of the mean and median of the 1D fft of the absolute difference between sin(x) and cos(x).
    """
    # Generate the sequence of tuples
    x = np.arange(range_start, range_end, step)
    sin_x = np.sin(x)
    cos_x = np.cos(x)
    abs_diff = np.abs(sin_x - cos_x)
    tuples = zip(x, sin_x, cos_x, abs_diff)

    # Plot the sine and cosine functions and the absolute difference
    fig, ax = plt.subplots()
    ax.plot(x, sin_x, label='sin(x)')
    ax.plot(x, cos_x, label='cos(x)')
    ax.plot(x, abs_diff, label='abs(sin(x) - cos(x))')
    ax.legend()

    # Compute the mean and median of the 1D fft of the absolute difference
    fft_abs_diff = fft(abs_diff)
    mean_fft = np.mean(fft_abs_diff)
    median_fft = np.median(fft_abs_diff)

    return tuples, ax, mean_fft, median_fft
range_start = -10
range_end = 10
step = 0.1