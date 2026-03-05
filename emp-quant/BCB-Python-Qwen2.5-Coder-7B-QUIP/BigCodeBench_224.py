
import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft

def task_func(range_start=-10, range_end=10, step=0.1):
    # Generate a sequence of tuples (x, sin(x), cos(x), abs(sin(x) - cos(x)))
    def generate_data():
        for x in np.arange(range_start, range_end, step):
            yield (x, np.sin(x), np.cos(x), abs(np.sin(x) - np.cos(x)))

    # Create a generator object
    generator = generate_data()

    # Plot the sine and cosine functions
    x_values = [x for x, _, _ in generator]
    sin_values = [np.sin(x) for x, _, _ in generator]
    cos_values = [np.cos(x) for x, _, _ in generator]
    abs_diff_values = [abs(np.sin(x) - np.cos(x)) for x, _, _ in generator]

    fig, ax = plt.subplots()
    ax.plot(x_values, sin_values, label='sin(x)')
    ax.plot(x_values, cos_values, label='cos(x)')
    ax.plot(x_values, abs_diff_values, label='abs(sin(x) - cos(x))')
    ax.legend()

    # Calculate the 1D FFT of the absolute difference
    fft_values = fft(abs_diff_values)

    # Calculate the mean and median of the FFT values
    mean_fft = np.mean(fft_values)
    median_fft = np.median(fft_values)

    # Return the results
    return generator, ax, abs(mean_fft), abs(median_fft)