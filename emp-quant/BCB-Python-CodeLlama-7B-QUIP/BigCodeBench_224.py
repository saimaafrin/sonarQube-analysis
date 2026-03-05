
import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft

def task_func(range_start=-10, range_end=10, step=0.1):
    # Generate a sequence of x values
    x = np.arange(range_start, range_end, step)

    # Generate a sequence of sin(x) and cos(x) values
    sin_x = np.sin(x)
    cos_x = np.cos(x)

    # Generate a sequence of abs(sin(x) - cos(x)) values
    abs_diff = np.abs(sin_x - cos_x)

    # Create a generator object that generates tuples of x, sin(x), cos(x), and abs(sin(x) - cos(x)) values
    generator = (x, sin_x, cos_x, abs_diff)

    # Plot the sine and cosine functions and the absolute difference between them
    ax = plt.subplot(111)
    ax.plot(x, sin_x, label='sin(x)')
    ax.plot(x, cos_x, label='cos(x)')
    ax.plot(x, abs_diff, label='abs(sin(x) - cos(x))')
    ax.legend()

    # Compute the mean and median of the 1D fft of the absolute difference between sin(x) and cos(x)
    fft_abs_diff = fft(abs_diff)
    mean = np.mean(fft_abs_diff)
    median = np.median(fft_abs_diff)

    return (generator, ax, mean, median)