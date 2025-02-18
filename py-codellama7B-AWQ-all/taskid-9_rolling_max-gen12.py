from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """

    rolling_max = []
    rolling_max.append(numbers[0])
    for i in range(len(numbers) - 1):
        if numbers[i] < numbers[i+1]:
            rolling_max.append(numbers[i+1])
        else:
            rolling_max.append(numbers[i])
    return rolling_max
