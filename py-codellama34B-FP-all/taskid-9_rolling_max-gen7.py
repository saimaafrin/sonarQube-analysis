from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """


    rolling_max = []
    max_value = 0
    for element in numbers:
        max_value = max(element, max_value)
        rolling_max.append(max_value)
    return rolling_max
