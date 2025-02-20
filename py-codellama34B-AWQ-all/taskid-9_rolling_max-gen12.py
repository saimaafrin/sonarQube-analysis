from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """

    rolling_max: List[int] = []
    max_value: int = 0
    for value in numbers:
        if value > max_value:
            max_value = value
        rolling_max.append(max_value)
    return rolling_max
