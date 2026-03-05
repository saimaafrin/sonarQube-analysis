import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft
def task_func(range_start=-10, range_end=10, step=0.1):
    """
    Generates a sequence of tuples containing x, sin(x), cos(x), and abs(sin(x) - cos(x)),
    plots the sine and cosine functions, and returns the plot along with the magnitude of the
    mean and median of the 1D fft of the absolute difference between the two functions.
    
    Parameters:
    - range_start: Start of the range for x values.
    - range_end: End of the range for x values.
    - step: Step size for the range of x values.
    
    Returns:
    - A tuple containing:
        - A generator object producing tuples in the format (x, sin(x), cos(x), abs(sin(x) - cos(x))).
        - An Axes object representing the plot.
        - The abs of the mean of the 1D fft of the absolute difference between sin(x) and cos(x).
        - The abs of the median of the 1D fft of the absolute difference between sin(x) and cos(x).
    """
    # Generate the sequence of tuples
    def generate_data():
        for x in np.arange(range_start, range_end, step):
            yield (x, np.sin(x), np.cos(x), abs(np.sin(x) - np.cos(x)))
    
    # Create the plot
    fig, ax = plt.subplots()
    x_values = []
    sin_values = []
    cos_values = []
    abs_diff_values = []
    
    for x, sin_x, cos_x, abs_diff in generate_data():
        x_values.append(x)
        sin_values.append(sin_x)
        cos_values.append(cos_x)
        abs_diff_values.append(abs_diff)
        ax.plot(x, sin_x, label='sin(x)')
        ax.plot(x, cos_x, label='cos(x)')
        ax.plot(x, abs_diff, label='abs(sin(x) - cos(x))')
    
    ax.legend()
    
    # Calculate the magnitude of the mean and median of the 1D fft of the absolute difference
    abs_diff_fft = np.abs(fft(abs_diff_values))
    mean_fft = np.mean(abs_diff_fft)
    median_fft = np.median(abs_diff_fft)
    
    return (generate_data(), ax, np.abs(mean_fft), np.abs(median_fft))