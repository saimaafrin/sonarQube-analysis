import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft
def task_func(range_start=-10, range_end=10, step=0.1):
    # Create a generator object
    def generate_data():
        x_values = np.arange(range_start, range_end, step)
        for x in x_values:
            yield (x, np.sin(x), np.cos(x), abs(np.sin(x) - np.cos(x)))

    # Generate data using the generator
    data = list(generate_data())

    # Extract x, sin(x), cos(x), and abs(sin(x) - cos(x)) values
    x = [d[0] for d in data]
    sin_x = [d[1] for d in data]
    cos_x = [d[2] for d in data]
    abs_diff = [d[3] for d in data]

    # Plot the sine and cosine functions
    fig, ax = plt.subplots()
    ax.plot(x, sin_x, label='sin(x)')
    ax.plot(x, cos_x, label='cos(x)')
    ax.plot(x, abs_diff, label='abs(sin(x) - cos(x))')
    ax.legend()

    # Calculate the magnitude of the mean and median of the 1D fft of the absolute difference
    fft_abs_diff = fft(abs_diff)
    mean_fft = np.mean(np.abs(fft_abs_diff))
    median_fft = np.median(np.abs(fft_abs_diff))

    return (generate_data(), ax, abs(mean_fft), abs(median_fft))