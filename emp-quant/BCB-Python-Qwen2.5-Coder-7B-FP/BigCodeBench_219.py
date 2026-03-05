import math
import statistics
import numpy as np
def task_func(input_list):
    # Sort the input list based on the degree value of its elements
    sorted_list = sorted(input_list, key=lambda x: x.degree)
    
    # Calculate the mean, median, and mode of the sorted list
    sorted_mean = round(statistics.mean([x.degree for x in sorted_list]))
    sorted_median = round(statistics.median([x.degree for x in sorted_list]))
    sorted_mode = round(statistics.mode([x.degree for x in sorted_list]))
    
    # Calculate the magnitude of the fast fourier transform of the degree values
    fft_values = np.fft.fft([x.degree for x in sorted_list])
    fft_magnitude = np.abs(fft_values)
    
    # Calculate the mean, median, and mode of the magnitude of the fast fourier transform
    fft_mean = round(statistics.mean(fft_magnitude))
    fft_median = round(statistics.median(fft_magnitude))
    fft_mode = round(statistics.mode(fft_magnitude))
    
    # Return the results as a tuple
    return (sorted_mean, sorted_median, sorted_mode, fft_mean, fft_median, fft_mode)