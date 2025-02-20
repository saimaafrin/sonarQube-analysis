from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """

    result = [0] * len(numbers)
    for i, current_value in enumerate(numbers):
        if i == 0:
            result[i] = current_value
        else:
            if current_value > numbers[i - 1]:
                result[i] = current_value
            else:
                result[i] = result[i - 1]
    return result
