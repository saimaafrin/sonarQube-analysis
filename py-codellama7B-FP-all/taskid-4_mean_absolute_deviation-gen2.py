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

    # calculate mean of this dataset
    mean = sum(numbers) / len(numbers)

    # calculate mean absolute deviation for each element in this dataset
    deviations = [abs(x - mean) for x in numbers]

    # return the average deviation for this dataset
    return sum(deviations) / len(deviations)
