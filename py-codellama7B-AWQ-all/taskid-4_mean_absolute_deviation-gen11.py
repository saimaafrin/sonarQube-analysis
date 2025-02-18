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


    # Calculate the mean of the input dataset
    mean = sum(numbers) / len(numbers)

    # Calculate the sum of absolute differences from the mean
    sum_of_absolute_diffs = 0.0
    for n in numbers:
        sum_of_absolute_diffs += abs(n - mean)

    # Divide the sum of differences by the length of the input dataset
    # to obtain the mean absolute deviation
    mean_abs_dev = sum_of_absolute_diffs / len(numbers)

    return mean_abs_dev
