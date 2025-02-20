from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """

    result = []
    for i in range(len(numbers)):
        max_current = numbers[i]
        for j in range(i):
            if numbers[j] > max_current:
                max_current = numbers[j]
        result.append(max_current)
    return result
