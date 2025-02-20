from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """

    rolling_max: List[int] = []
    current_max: int = 0

    for number in numbers:
        current_max = max(current_max, number)
        rolling_max.append(current_max)

    return rolling_max
