from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """

    result = []
    current_max = numbers[0]
    result.append(current_max)
    for number in numbers[1:]:
        current_max = max(current_max, number)
        result.append(current_max)
    return result
