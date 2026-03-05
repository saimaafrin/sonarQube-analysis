import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft
def task_func(range_start=-10, range_end=10, step=0.1):
    # Generate a sequence of tuples containing x, sin(x), cos(x), and abs(sin(x) - cos(x)) values
    x = np.arange(range_start, range_end, step)
    y_sin = np.sin(x)
    y_cos = np.cos(x)
    y_abs = np.abs(y_sin - y_cos)
    tuples = zip(x, y_sin, y_cos, y_abs)

    # Plot the sine and cosine functions and the absolute difference between them
    fig, ax = plt.subplots()
    ax.plot(x, y_sin, label='sin(x)')
    ax.plot(x, y_cos, label='cos(x)')
    ax.plot(x, y_abs, label='abs(sin(x) - cos(x))')
    ax.legend()

    # Compute the mean and median of the 1D fft of the absolute difference between sin(x) and cos(x)
    fft_abs_diff = fft(y_abs)
    mean_fft_abs_diff = np.mean(fft_abs_diff)
    median_fft_abs_diff = np.median(fft_abs_diff)

    # Return the generator, Axes object, and the mean and median of the 1D fft of the absolute difference between sin(x) and cos(x)
    return tuples, ax, mean_fft_abs_diff, median_fft_abs_diff
range_start = -10
range_end = 10
step = 0.1