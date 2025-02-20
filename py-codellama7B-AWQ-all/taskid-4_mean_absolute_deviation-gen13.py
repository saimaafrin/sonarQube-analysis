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

    numbers_centered_on_mean = [x - numbers[0] for x in numbers]
    # 1. Calculate the Mean of the dataset
    sum_numbers = sum(numbers_centered_on_mean)
    numbers_count = len(numbers)
    mean_of_numbers = sum_numbers / numbers_count

    # 2. Calculate the Mean Absolute Deviation
    sum_of_absolute_deviations = 0.0
    for element in numbers_centered_on_mean:
        sum_of_absolute_deviations += abs(element - mean_of_numbers)

    return sum_of_absolute_deviations / numbers_count
\end{code}
