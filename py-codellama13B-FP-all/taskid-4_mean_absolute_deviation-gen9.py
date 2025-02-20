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

    # Calculate the mean of this dataset
    mean = sum(numbers) / len(numbers)

    # Initialize sum of absolute deviations
    deviation_sum = 0.0

    # Loop through numbers, calculating absolute deviations and summing them
    for number in numbers:
        absolute_deviation = abs(number - mean)
        deviation_sum += absolute_deviation

    # Calculate and return mean absolute deviation
    return deviation_sum / len(numbers)
