from typing import List

def mean_absolute_deviation(numbers: List[float]) -> float:
    """ For a given list of input numbers, calculate Mean Absolute Deviation
    around the mean of this dataset.
    Mean Absolute Deviation is the average absolute difference between each
    element and a centerpoint (mean in this case):
    MAD = average | x - x_mean |
    >>> mean_absolute_deviation([1.0, 2.0, 3.0, 4.0])
    1.0
    """


    # Calculate mean of input numbers
    numbers_sum = sum(numbers)
    numbers_len = len(numbers)
    numbers_mean = numbers_sum / numbers_len

    # Calculate absolute difference between each element and mean
    diff_abs_list = [abs(number - numbers_mean) for number in numbers]

    # Calculate mean of absolute differences
    diff_abs_sum = sum(diff_abs_list)
    diff_abs_mean = diff_abs_sum / numbers_len

    return diff_abs_mean
