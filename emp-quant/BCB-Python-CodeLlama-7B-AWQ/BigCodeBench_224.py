import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft
def task_func(range_start=-10, range_end=10, step=0.1):
    """
    Generates a sequence of tuples containing x, sin(x), cos(x), and abs(sin(x) - cos(x)) values.
    Plots the sine and cosine functions using these values along with the absolute difference between the two functions.
    Returns the plot and the abs of the mean and median of the 1D fft of the absolute difference between sin(x) and cos(x).
    """
    # Generate the sequence of tuples
    x = np.arange(range_start, range_end, step)
    y_sin = np.sin(x)
    y_cos = np.cos(x)
    y_abs = np.abs(y_sin - y_cos)

    # Create the plot
    fig, ax = plt.subplots()
    ax.plot(x, y_sin, label='sin(x)')
    ax.plot(x, y_cos, label='cos(x)')
    ax.plot(x, y_abs, label='abs(sin(x) - cos(x))')
    ax.legend()

    # Compute the mean and median of the 1D fft of the absolute difference
    fft_abs_diff = fft(y_abs)
    mean_fft_abs_diff = np.mean(np.abs(fft_abs_diff))
    median_fft_abs_diff = np.median(np.abs(fft_abs_diff))

    return (x, y_sin, y_cos, y_abs), ax, mean_fft_abs_diff, median_fft_abs_diff
range_start = -10
range_end = 10
step = 0.1