
import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft

def task_func(range_start=-10, range_end=10, step=0.1):
    # Create a generator object
    def generate_data():
        x_values = np.arange(range_start, range_end, step)
        for x in x_values:
            yield (x, np.sin(x), np.cos(x), abs(np.sin(x) - np.cos(x)))
    
    # Generate the data
    data_generator = generate_data()
    
    # Extract x, sin(x), cos(x), and abs(sin(x) - cos(x)) values
    x_values = []
    sin_values = []
    cos_values = []
    abs_diff_values = []
    for data in data_generator:
        x_values.append(data[0])
        sin_values.append(data[1])
        cos_values.append(data[2])
        abs_diff_values.append(data[3])
    
    # Plot the sine and cosine functions
    fig, ax = plt.subplots()
    ax.plot(x_values, sin_values, label='sin(x)')
    ax.plot(x_values, cos_values, label='cos(x)')
    ax.plot(x_values, abs_diff_values, label='abs(sin(x) - cos(x))')
    ax.legend()
    
    # Calculate the 1D fft of the absolute difference
    fft_values = fft(abs_diff_values)
    
    # Calculate the mean and median of the fft values
    mean_fft = np.mean(fft_values)
    median_fft = np.median(fft_values)
    
    # Return the results
    return (x_values, sin_values, cos_values, abs_diff_values), ax, abs(mean_fft), abs(median_fft)