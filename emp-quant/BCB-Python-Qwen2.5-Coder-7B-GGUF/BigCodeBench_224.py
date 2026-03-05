
import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft

def task_func(range_start=-10, range_end=10, step=0.1):
    # Create a generator object
    def generator():
        x_values = np.arange(range_start, range_end, step)
        for x in x_values:
            yield (x, np.sin(x), np.cos(x), abs(np.sin(x) - np.cos(x)))

    # Generate the sequence of tuples
    gen = generator()
    data = [next(gen) for _ in range(len(np.arange(range_start, range_end, step)))]

    # Plot the sine and cosine functions
    x = [d[0] for d in data]
    sin_x = [d[1] for d in data]
    cos_x = [d[2] for d in data]
    diff = [d[3] for d in data]

    fig, ax = plt.subplots()
    ax.plot(x, sin_x, label='sin(x)')
    ax.plot(x, cos_x, label='cos(x)')
    ax.plot(x, diff, label='abs(sin(x) - cos(x))')
    ax.legend()

    # Calculate the magnitude of the mean and median of the 1D fft of the absolute difference
    fft_diff = fft(diff)
    mean_fft = np.mean(np.abs(fft_diff))
    median_fft = np.median(np.abs(fft_diff))

    return (gen, ax, mean_fft, median_fft)