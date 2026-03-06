
import math
import statistics
import numpy as np

def task_func(input_list):
    # Sort the input list based on the degree value of its elements
    sorted_list = sorted(input_list)
    
    # Calculate the mean, median, and mode of the sorted list
    sorted_mean = round(statistics.mean(sorted_list))
    sorted_median = round(statistics.median(sorted_list))
    sorted_mode = round(statistics.mode(sorted_list))
    
    # Calculate the FFT of the degree values
    fft_values = np.fft.fft(sorted_list)
    fft_magnitude = np.abs(fft_values)
    
    # Calculate the mean, median, and mode of the FFT magnitudes
    fft_mean = round(np.mean(fft_magnitude))
    fft_median = round(np.median(fft_magnitude))
    
    # Find the mode of the FFT magnitudes
    try:
        fft_mode = round(statistics.mode(fft_magnitude))
    except statistics.StatisticsError:
        # If there's no unique mode, set it to None
        fft_mode = None
    
    # Return the results as a tuple
    return (sorted_mean, sorted_median, sorted_mode, fft_mean, fft_median, fft_mode)