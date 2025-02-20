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

    # Find mean of input dataset
    dataset_mean = sum(numbers) / len(numbers)

    # Calculate sum of absolute differences to mean
    absolute_deviation = 0.0
    for number in numbers:
        absolute_deviation += abs(number - dataset_mean)

    # Return MAD as average absolute deviation
    return absolute_deviation / len(numbers)
