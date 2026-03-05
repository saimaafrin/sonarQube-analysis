
import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft

def task_func(range_start=-10, range_end=10, step=0.1):
    # Generate a sequence of tuples containing x, sin(x), cos(x), and abs(sin(x) - cos(x))
    x = np.arange(range_start, range_end, step)
    y_sin = np.sin(x)
    y_cos = np.cos(x)
    y_diff = np.abs(y_sin - y_cos)
    z = np.column_stack((x, y_sin, y_cos, y_diff))

    # Plot the sine and cosine functions and the absolute difference between them
    fig, ax = plt.subplots()
    ax.plot(x, y_sin, label='sin(x)')
    ax.plot(x, y_cos, label='cos(x)')
    ax.plot(x, y_diff, label='abs(sin(x) - cos(x))')
    ax.legend()

    # Compute the mean and median of the 1D fft of the absolute difference between sin(x) and cos(x)
    fft_abs_diff = fft(y_diff)
    mean_fft_abs_diff = np.mean(np.abs(fft_abs_diff))
    median_fft_abs_diff = np.median(np.abs(fft_abs_diff))

    return z, ax, mean_fft_abs_diff, median_fft_abs_diff

# Generate the sequence of tuples and plot the sine and cosine functions
z, ax, mean_fft_abs_diff, median_fft_abs_diff = task_func()

# Print the results
print(f'Mean of 1D fft of abs(sin(x) - cos(x)): {mean_fft_abs_diff:.2f}')
print(f'Median of 1D fft of abs(sin(x) - cos(x)): {median_fft_abs_diff:.2f}')