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

    numbers = map(float, numbers)
    numbers_count = len(numbers)
    if numbers_count < 1:
        raise ValueError('empty list')
    mean = sum(numbers) / numbers_count
    return sum(abs(mean - x) for x in numbers) / numbers_count
