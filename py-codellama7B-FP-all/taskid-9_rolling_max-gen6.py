from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """

    rolling_max = []

    for i in range(len(numbers)):
        max_ = max(numbers[i], numbers[i] if len(rolling_max) == 0 else rolling_max[-1])
        rolling_max.append(max_)

    return rolling_max
