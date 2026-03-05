import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft
def task_func(range_start=-10, range_end=10, step=0.1):
    # Create a generator object
    def generator():
        x_values = np.arange(range_start, range_end, step)
        for x in x_values:
            yield (x, np.sin(x), np.cos(x), abs(np.sin(x) - np.cos(x)))

    # Generate data using the generator
    gen = generator()
    data = list(gen)
    x, sin_x, cos_x, abs_diff = zip(*data)

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

    return (generator(), ax, abs(mean_fft), abs(median_fft))