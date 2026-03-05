
import math
import statistics
import numpy as np

def task_func(input_list):
    # Sort the list in ascending order based on the degree value
    sorted_list = sorted(input_list, key=lambda x: x[1])

    # Calculate the mean, median, and mode of the sorted list
    mean = statistics.mean(sorted_list)
    median = statistics.median(sorted_list)
    mode = statistics.mode(sorted_list)

    # Calculate the mean, median, and mode of the magnitude of the fast Fourier transform of the degree values
    # using the numpy library
    fft_degrees = np.abs(np.fft.fft(sorted_list))
    fft_mean = statistics.mean(fft_degrees)
    fft_median = statistics.median(fft_degrees)
    fft_mode = statistics.mode(fft_degrees)

    return (mean, median, mode, fft_mean, fft_median, fft_mode)