import math
import statistics
import numpy as np
def task_func(input_list):
    """
    Sorts the input list in ascending order based on the degree value of its elements, and then 
    calculates the mean, median, and mode of both the sorted list and the same for the magnitude of 
    the fast fourier transform of the degree values upto the nearest integer.

    Parameters:
    input_list (list): A list of numbers to be sorted and analyzed.

    Returns:
    tuple: A tuple containing the rounded mean, median and mode of the sorted list along with those 
    for the magnitude of the fast fourier transform of the degree values.

    Requirements:
    - math
    - statistics
    - numpy

    Example:
    >>> input_list = [30, 45, 60, 90, 180]
    >>> stats = task_func(input_list)
    >>> print(stats)
    (81, 60, 30, 10712, 8460, 8460)
    """
    # Sort the input list in ascending order based on the degree value of its elements
    sorted_list = sorted(input_list, key=lambda x: math.degrees(x))

    # Calculate the mean, median and mode of the sorted list
    mean = statistics.mean(sorted_list)
    median = statistics.median(sorted_list)
    mode = statistics.mode(sorted_list)

    # Calculate the mean, median and mode of the magnitude of the fast fourier transform of the degree values
    fft_list = np.fft.fft(sorted_list)
    fft_abs_list = np.abs(fft_list)
    fft_abs_list = np.round(fft_abs_list)
    fft_abs_list = fft_abs_list.astype(int)
    fft_abs_list = sorted(fft_abs_list, key=lambda x: x)
    fft_abs_mean = statistics.mean(fft_abs_list)
    fft_abs_median = statistics.median(fft_abs_list)
    fft_abs_mode = statistics.mode(fft_abs_list)

    return mean, median, mode, fft_abs_mean, fft_abs_median, fft_abs_mode