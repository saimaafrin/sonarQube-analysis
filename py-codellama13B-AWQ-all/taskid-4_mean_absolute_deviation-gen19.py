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


    # calculate the mean of the list of numbers
    mean = sum(numbers) / float(len(numbers))

    # calculate the absolute deviations from the mean
    absolute_deviations = [abs(x - mean) for x in numbers]

    # calculate the average of the absolute deviations
    average_absolute_deviation = sum(absolute_deviations) / float(len(numbers))

    return average_absolute_deviation
