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

    # Calculate the mean of the dataset first
    mean = sum(numbers) / len(numbers)

    # Then calculate the absolute difference between each element and mean
    differences = [abs(x - mean) for x in numbers]

    # Calculate the mean of the absolute differences
    mean_of_differences = sum(differences) / len(differences)

    return mean_of_differences
