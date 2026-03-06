
import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft

def task_func(range_start=-10, range_end=10, step=0.1):
    # Create a generator object
    def generate_data():
        for x in np.arange(range_start, range_end, step):
            yield (x, np.sin(x), np.cos(x), abs(np.sin(x) - np.cos(x)))

    # Generate data using the generator
    data = list(generate_data())

    # Extract x, sin(x), cos(x), and abs(sin(x) - cos(x)) values
    x_values = [d[0] for d in data]
    sin_values = [d[1] for d in data]
    cos_values = [d[2] for d in data]
    diff_values = [d[3] for d in data]

    # Plot the sine and cosine functions
    fig, ax = plt.subplots()
    ax.plot(x_values, sin_values, label='sin(x)')
    ax.plot(x_values, cos_values, label='cos(x)')
    ax.legend()

    # Calculate the absolute difference between sin(x) and cos(x)
    diff_fft = fft(diff_values)

    # Calculate the mean and median of the absolute difference's FFT
    mean_fft = np.mean(np.abs(diff_fft))
    median_fft = np.median(np.abs(diff_fft))

    return (
        generate_data(),  # Generator object
        ax,               # Axes object
        abs(mean_fft),      # Absolute value of the mean of the FFT
        abs(median_fft)   # Absolute value of the median of the FFT
    )